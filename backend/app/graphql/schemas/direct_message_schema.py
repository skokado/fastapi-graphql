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
    created_at: datetime

    receiver_id: int
    sender_id: int
    text: str
