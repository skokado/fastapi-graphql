from typing import Optional

import strawberry

from .schemas import DirectMessage, User
from ..resolvers import direct_message as direct_message_resolver
from ..resolvers import users as users_resolver


@strawberry.type
class Query:
    get_user: Optional[User] = strawberry.field(resolver=users_resolver.get)
    list_users: list[User] = strawberry.field(resolver=users_resolver.list)

    get_messages: list[DirectMessage] = strawberry.field(resolver=direct_message_resolver.get_messages)
