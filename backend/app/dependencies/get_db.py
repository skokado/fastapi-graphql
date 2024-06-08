from typing import AsyncGenerator
from sqlalchemy.orm import Session

from app.config.db import SessionLocal


async def get_db() -> AsyncGenerator[Session, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
