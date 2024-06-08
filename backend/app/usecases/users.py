from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.graphql.schemas.user_schema import UserRequest

from ..models import User


async def list(prefix: Optional[str] = None, db: Session = Depends(get_db)) -> list[User]:
    if prefix:
        return db.query(User).filter(User.username.startswith(prefix)).all()
    return db.query(User).all()


async def get(user_id: int, db: Session = Depends(get_db)) -> Optional[User]:
    return db.query(User).get(user_id)


async def create(data: UserRequest, db: Session = Depends(get_db)) -> User:
    user = User(username=data.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
