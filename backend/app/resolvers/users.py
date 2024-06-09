from typing import Optional

import strawberry

from ..models import User as UserModel
from ..usecases import users as usecase
from ..graphql.schemas.user_schema import UserRequest


async def get(info: strawberry.Info, user_id: int) -> Optional[UserModel]:
    user = await usecase.get(user_id, info.context.db)
    return user


async def list(info: strawberry.Info, prefix: Optional[str] = None) -> list[UserModel]:
    return await usecase.list(prefix, info.context.db)


async def create(data: UserRequest, info: strawberry.Info) -> UserModel:
    return await usecase.create(data, info.context.db)
