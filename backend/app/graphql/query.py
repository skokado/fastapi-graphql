import strawberry

from .schemas.user_schema import User
from ..resolvers import users as users_resolver


@strawberry.type
class Query:
    user: User = strawberry.field(resolver=users_resolver.get)
    users: list[User] = strawberry.field(resolver=users_resolver.list)
