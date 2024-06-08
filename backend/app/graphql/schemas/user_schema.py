import strawberry


@strawberry.input
class UserRequest:
    username: str


@strawberry.type
class UserResponse:
    id: int
    username: str
