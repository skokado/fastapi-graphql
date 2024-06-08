from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .schemas import graphql_schema
from .dependencies import get_context

app = FastAPI(title="Chat App with FastAPI", debug=True)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}


graphql_router = GraphQLRouter(schema=graphql_schema, context_getter=get_context)
app.include_router(graphql_router, prefix="/graphql", tags=["GraphQL"])
