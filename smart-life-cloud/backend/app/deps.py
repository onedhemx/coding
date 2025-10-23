from __future__ import annotations

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from .database import get_session
from .models import User, Membership, Role
from .security import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
    try:
        data = decode_token(token)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = session.get(User, data.get("user_id"))
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")
    return user


def require_roles(roles: list[Role]):
    def checker(user: User = Depends(get_current_user), session: Session = Depends(get_session)) -> User:
        # For simplicity, pick first membership; real implementation should be per-org
        membership = session.exec(select(Membership).where(Membership.user_id == user.id)).first()
        if not membership or membership.role not in roles:
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user

    return checker
