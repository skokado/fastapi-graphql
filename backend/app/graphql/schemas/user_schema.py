import strawberry


@strawberry.input
class UserRequest:
    username: str


@strawberry.type
class User:
    id: int
    username: str
