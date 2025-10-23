from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..database import get_session
from ..deps import get_current_user, require_roles
from ..models import Device, Membership, Role, User
from ..schemas import DeviceCreate, DeviceRead

router = APIRouter(prefix="/devices", tags=["devices"])


def _assert_membership(session: Session, user_id: int, org_id: int) -> None:
    membership = session.exec(
        select(Membership).where(Membership.user_id == user_id, Membership.organization_id == org_id)
    ).first()
    if not membership:
        raise HTTPException(status_code=404, detail="Organization not found or access denied")


@router.get("", response_model=list[DeviceRead])
def list_devices(
    org_id: int = Query(..., description="Organization ID"),
    site_id: Optional[int] = Query(None, description="Filter by site ID"),
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    _assert_membership(session, user.id, org_id)
    stmt = select(Device).where(Device.organization_id == org_id)
    if site_id is not None:
        stmt = stmt.where(Device.site_id == site_id)
    return session.exec(stmt).all()


@router.post("", response_model=DeviceRead, dependencies=[Depends(require_roles([Role.OWNER, Role.ADMIN]))])
def create_device(payload: DeviceCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    _assert_membership(session, user.id, payload.organization_id)
    dev = Device(
        organization_id=payload.organization_id,
        site_id=payload.site_id,
        device_uid=payload.device_uid,
        name=payload.name,
        status=False,
        last_seen_at=None,
    )
    session.add(dev)
    session.flush()
    return dev


@router.get("/{device_id}", response_model=DeviceRead)
def get_device(device_id: int, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    dev = session.get(Device, device_id)
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership(session, user.id, dev.organization_id)
    return dev


@router.post("/{device_id}/command/toggle", response_model=DeviceRead)
def toggle_device(device_id: int, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    dev = session.get(Device, device_id)
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    _assert_membership(session, user.id, dev.organization_id)
    dev.status = not dev.status
    dev.last_seen_at = datetime.now(timezone.utc)
    session.add(dev)
    session.flush()
    return dev
