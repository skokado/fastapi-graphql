import strawberry

from .mutation import Mutation
from .query import Query


graphql_schema = strawberry.Schema(query=Query, mutation=Mutation)
