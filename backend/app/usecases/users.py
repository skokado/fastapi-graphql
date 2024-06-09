from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.graphql.schemas.user_schema import UserRequest

from ..models import User


async def list(prefix: Optional[str] = None, db: Session = Depends(get_db)) -> list[User]:
    stmt = select(User)
    if prefix:
        stmt = stmt.filter(User.username.startswith(prefix))
        return db.scalars(stmt).all()
    return db.scalars(stmt).all()


async def get(user_id: int, db: Session = Depends(get_db)) -> Optional[User]:
    stmt = select(User).where(User.id == user_id)
    return db.scalar(stmt)


async def create(data: UserRequest, db: Session = Depends(get_db)) -> User:
    user = User(username=data.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
