import strawberry

from .schemas.user_schema import UserResponse
from ..resolvers import users as users_resolver


@strawberry.type
class Query:
    user: UserResponse = strawberry.field(resolver=users_resolver.get)
    users: list[UserResponse] = strawberry.field(resolver=users_resolver.list)
