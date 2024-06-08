import strawberry

from .user_schema import UserResponse
from ...resolvers import users as users_resolver


@strawberry.type
class Mutation:
    create_user: UserResponse = strawberry.mutation(resolver=users_resolver.create)
