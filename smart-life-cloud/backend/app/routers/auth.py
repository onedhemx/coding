from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from ..database import get_session
from ..models import User, Organization, Membership, Role
from ..schemas import Token, UserCreate, UserRead
from ..security import get_password_hash, verify_password, create_access_token
from ..deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(UserCreate):
    org_name: str | None = None


@router.post("/register", response_model=Token)
def register(payload: RegisterRequest, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(email=payload.email, password_hash=get_password_hash(payload.password))
    session.add(user)
    session.flush()

    if payload.org_name:
        org = Organization(name=payload.org_name)
        session.add(org)
        session.flush()
        session.add(Membership(user_id=user.id, organization_id=org.id, role=Role.OWNER))

    token = create_access_token(subject={"user_id": user.id, "email": user.email})
    return Token(access_token=token)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")

    token = create_access_token(subject={"user_id": user.id, "email": user.email})
    return Token(access_token=token)


@router.get("/me", response_model=UserRead)
def me(user: User = Depends(get_current_user)):
    return user
