from typing import Optional

import strawberry

from .schemas.user_schema import User
from ..resolvers import users as users_resolver


@strawberry.type
class Query:
    get_user: Optional[User] = strawberry.field(resolver=users_resolver.get)
    list_users: list[User] = strawberry.field(resolver=users_resolver.list)
