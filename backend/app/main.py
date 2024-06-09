from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .graphql import graphql_schema
from .dependencies import get_context

app = FastAPI(title="Chat App with FastAPI", debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}


graphql_router = GraphQLRouter(schema=graphql_schema, context_getter=get_context)
app.include_router(graphql_router, prefix="/graphql", tags=["GraphQL"])
