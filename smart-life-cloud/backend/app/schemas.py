from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Any

from pydantic import BaseModel, EmailStr

from .models import Role


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: int
    email: EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class OrganizationCreate(BaseModel):
    name: str


class OrganizationRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class MembershipRead(BaseModel):
    user_id: int
    organization_id: int
    role: Role


class DeviceCreate(BaseModel):
    organization_id: int
    site_id: Optional[int] = None
    device_uid: str
    name: str


class DeviceRead(BaseModel):
    id: int
    organization_id: int
    site_id: Optional[int]
    device_uid: str
    name: str
    status: bool
    last_seen_at: Optional[datetime]

    class Config:
        from_attributes = True

class TelemetryPoint(BaseModel):
    ts: datetime
    payload_json: Any


class TelemetryIngest(BaseModel):
    device_uid: str
    points: List[TelemetryPoint]


class TelemetryStats(BaseModel):
    metric: str
    count: int
    min_value: Optional[float] = None
    min_ts: Optional[datetime] = None
    max_value: Optional[float] = None
    max_ts: Optional[datetime] = None
    avg_value: Optional[float] = None


class EventRead(BaseModel):
    id: int
    device_id: int
    ts: datetime
    type: str
    severity: str
    message: str

    class Config:
        from_attributes = True
