from __future__ import annotations

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..database import get_session
from ..deps import get_current_user
from ..models import Event, Device, Membership, User
from ..schemas import EventRead

router = APIRouter(prefix="/events", tags=["events"])


def _assert_membership_by_device(session: Session, user_id: int, device: Device) -> None:
    membership = session.exec(
        select(Membership).where(Membership.user_id == user_id, Membership.organization_id == device.organization_id)
    ).first()
    if not membership:
        raise HTTPException(status_code=404, detail="Device not found or access denied")


@router.get("/{device_id}", response_model=list[EventRead])
def list_events(
    device_id: int,
    frm: Optional[datetime] = Query(None, alias="from"),
    to: Optional[datetime] = None,
    limit: int = 200,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership_by_device(session, user.id, device)

    stmt = select(Event).where(Event.device_id == device_id)
    if frm is not None:
        stmt = stmt.where(Event.ts >= frm)
    if to is not None:
        stmt = stmt.where(Event.ts <= to)
    stmt = stmt.order_by(Event.ts.desc()).limit(min(max(limit, 1), 2000))

    rows = session.exec(stmt).all()
    return rows


@router.post("/{device_id}")
def create_event(
    device_id: int,
    type: str,
    severity: str,
    message: str,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership_by_device(session, user.id, device)

    ev = Event(device_id=device_id, ts=datetime.utcnow(), type=type, severity=severity, message=message)
    session.add(ev)
    session.flush()
    return {"status": "ok", "id": ev.id}
