import strawberry

from .mutation import Mutation
from .subscription import Subscription
from .query import Query


graphql_schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
