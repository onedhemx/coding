from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..database import get_session
from ..deps import get_current_user
from ..models import Organization, Membership, User, Role
from ..schemas import OrganizationCreate, OrganizationRead

router = APIRouter(prefix="/orgs", tags=["organizations"])


@router.get("/me", response_model=list[OrganizationRead])
def list_my_orgs(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    memberships = session.exec(select(Membership).where(Membership.user_id == user.id)).all()
    if not memberships:
        return []
    org_ids = [m.organization_id for m in memberships]
    orgs = session.exec(select(Organization).where(Organization.id.in_(org_ids))).all()
    return orgs


@router.post("", response_model=OrganizationRead)
def create_org(payload: OrganizationCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    org = Organization(name=payload.name)
    session.add(org)
    session.flush()

    # creator becomes OWNER
    session.add(Membership(user_id=user.id, organization_id=org.id, role=Role.OWNER))
    session.flush()

    return org


@router.get("/{org_id}", response_model=OrganizationRead)
def get_org(org_id: int, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    # ensure user is a member of org
    membership = session.exec(
        select(Membership).where(Membership.user_id == user.id, Membership.organization_id == org_id)
    ).first()
    if not membership:
        raise HTTPException(status_code=404, detail="Organization not found")

    org = session.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org
