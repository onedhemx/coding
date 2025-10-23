from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


def init_db() -> None:
    # Import models so SQLModel knows about them
    from . import models  # noqa: F401
    SQLModel.metadata.create_all(engine)


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_session() -> Generator[Session, None, None]:
    with session_scope() as s:
        yield s
