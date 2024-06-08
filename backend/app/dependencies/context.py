import redis.asyncio as redis
from fastapi import Depends
from strawberry.fastapi import BaseContext
from sqlalchemy.orm import Session

from .get_db import get_db
from .get_redis import get_redis


class DIContext(BaseContext):
    def __init__(self, db: Session, redis: redis.Redis):
        self.db = db
        self.redis = redis


async def get_context(db: Session = Depends(get_db), redis: redis.Redis = Depends(get_redis)) -> DIContext:
    return DIContext(
        db=db,
        redis=redis,
    )
