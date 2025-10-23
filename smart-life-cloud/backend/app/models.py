from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import JSON as SQLiteJSON
from sqlmodel import Field, SQLModel


class Role(str, Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    TECH = "TECH"
    VIEWER = "VIEWER"


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Membership(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", primary_key=True)
    role: Role


class Site(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", index=True)
    name: str
    address: Optional[str] = None


class Device(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", index=True)
    site_id: Optional[int] = Field(default=None, foreign_key="site.id", index=True)
    device_uid: str = Field(index=True)
    name: str
    status: bool = Field(default=False)
    last_seen_at: Optional[datetime] = None


class DeviceConfig(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="device.id", index=True)
    config_json: dict = Field(sa_column=Column("json", SQLiteJSON))
    version: int = 1
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Telemetry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="device.id", index=True)
    ts: datetime = Field(index=True)
    payload_json: dict = Field(sa_column=Column(SQLiteJSON))


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="device.id", index=True)
    ts: datetime = Field(index=True)
    type: str
    severity: str
    message: str
