from datetime import datetime

import strawberry


@strawberry.input
class DirectMessageRequest:
    receiver_id: int
    sender_id: int
    text: str


@strawberry.type
class DirectMessage:
    id: int
    created_at: str  # TODO How to handle datetime in Redis Broker?

    receiver_id: int
    sender_id: int
    text: str
