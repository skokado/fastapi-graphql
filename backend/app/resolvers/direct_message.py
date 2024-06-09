from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
import strawberry

from app.dependencies import get_db
from app.models import DirectMessage


async def get_messages(receiver_id: int, sender_id: int, info: strawberry.Info) -> list[DirectMessage]:
    db = info.context.db

    stmt = (
        select(DirectMessage)
        .where(
            DirectMessage.receiver_id == receiver_id,
            DirectMessage.sender_id == sender_id,
        )
        .order_by(DirectMessage.created_at.desc())
    )
    return db.scalars(stmt).all()


async def get_latest_message(receiver_id: int, sender_id: int, db: Session = Depends(get_db)) -> Optional[DirectMessage]:
    stmt = (
        select(DirectMessage)
        .where(
            DirectMessage.receiver_id == receiver_id,
            DirectMessage.sender_id == sender_id,
        )
        .order_by(DirectMessage.created_at.desc())
    )
    return db.scalar(stmt)
