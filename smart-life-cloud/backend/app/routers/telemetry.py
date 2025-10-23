from __future__ import annotations

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..database import get_session
from ..deps import get_current_user
from ..models import Telemetry, Device, Membership, User
from ..schemas import TelemetryIngest, TelemetryPoint, TelemetryStats

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


def _assert_membership_by_device(session: Session, user_id: int, device: Device) -> None:
    membership = session.exec(
        select(Membership).where(
            Membership.user_id == user_id,
            Membership.organization_id == device.organization_id,
        )
    ).first()
    if not membership:
        raise HTTPException(status_code=404, detail="Device not found or access denied")


@router.post("/ingest")
def ingest(payload: TelemetryIngest, session: Session = Depends(get_session)):
    device = session.exec(select(Device).where(Device.device_uid == payload.device_uid)).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not registered")

    for p in payload.points:
        rec = Telemetry(device_id=device.id, ts=p.ts, payload_json=p.payload_json)
        session.add(rec)
    session.flush()
    return {"status": "ok", "inserted": len(payload.points)}


@router.get("/{device_id}", response_model=list[TelemetryPoint])
def get_telemetry(
    device_id: int,
    frm: Optional[datetime] = Query(None, alias="from"),
    to: Optional[datetime] = None,
    limit: int = 500,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership_by_device(session, user.id, device)

    stmt = select(Telemetry).where(Telemetry.device_id == device_id)
    if frm is not None:
        stmt = stmt.where(Telemetry.ts >= frm)
    if to is not None:
        stmt = stmt.where(Telemetry.ts <= to)

    stmt = stmt.order_by(Telemetry.ts.desc()).limit(min(max(limit, 1), 5000))
    rows = session.exec(stmt).all()
    # return ascending by time for charting
    rows = list(reversed(rows))
    return [TelemetryPoint(ts=r.ts, payload_json=r.payload_json) for r in rows]


def _get_metric_value(payload: dict, path: str) -> Optional[float]:
    # Support dot-notation for nested keys, e.g., "env.temperature"
    try:
        cur: object = payload
        for part in path.split('.'):
            if not isinstance(cur, dict) or part not in cur:
                return None
            cur = cur[part]
        if isinstance(cur, (int, float)):
            return float(cur)
        return None
    except Exception:
        return None


@router.get("/{device_id}/stats", response_model=TelemetryStats)
def get_telemetry_stats(  # type: ignore[func-returns-value]
    device_id: int,
    metric: str = Query(..., description="Metric key in payload_json (dot notation supported)"),
    frm: Optional[datetime] = Query(None, alias="from"),
    to: Optional[datetime] = None,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership_by_device(session, user.id, device)

    stmt = select(Telemetry).where(Telemetry.device_id == device_id)
    if frm is not None:
        stmt = stmt.where(Telemetry.ts >= frm)
    if to is not None:
        stmt = stmt.where(Telemetry.ts <= to)
    stmt = stmt.order_by(Telemetry.ts.desc()).limit(10000)

    rows = session.exec(stmt).all()

    count = 0
    min_val: Optional[float] = None
    min_ts: Optional[datetime] = None
    max_val: Optional[float] = None
    max_ts: Optional[datetime] = None
    sum_val: float = 0.0

    for r in rows:
        v = _get_metric_value(r.payload_json, metric)
        if v is None:
            continue
        count += 1
        sum_val += v
        if min_val is None or v < min_val:
            min_val = v
            min_ts = r.ts
        if max_val is None or v > max_val:
            max_val = v
            max_ts = r.ts

    avg_val: Optional[float] = (sum_val / count) if count > 0 else None
    return TelemetryStats(
        metric=metric,
        count=count,
        min_value=min_val,
        min_ts=min_ts,
        max_value=max_val,
        max_ts=max_ts,
        avg_value=avg_val,
    )
