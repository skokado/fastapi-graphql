from fastapi import Depends
from strawberry.fastapi import BaseContext
from sqlalchemy.orm import Session

from .get_db import get_db


class DIContext(BaseContext):
    def __init__(self, db: Session):
        self.db = db


async def get_context(db: Session = Depends(get_db)) -> DIContext:
    return DIContext(db)
