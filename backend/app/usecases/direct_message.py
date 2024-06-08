from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from ..models import DirectMessage
from ..graphql.schemas import DirectMessageRequest


async def create_dm(data: DirectMessageRequest, db: Session = Depends(get_db)) -> DirectMessage:
    new_dm = DirectMessage(
        sender_id=data.sender_id,
        receiver_id=data.receiver_id,
        text=data.text,
    )
    db.add(new_dm)
    db.commit()
    db.refresh(new_dm)
    return new_dm
