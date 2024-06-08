import asyncio
from typing import AsyncGenerator, Optional

import strawberry

from app.models import DirectMessage
from .schemas import DirectMessage


async def count_resolver(target: int = 10) -> AsyncGenerator[int, None]:
    for i in range(1, target + 1):
        yield i
        await asyncio.sleep(0.5)


@strawberry.type
class Subscription:
    count = strawberry.subscription(resolver=count_resolver)

    @strawberry.subscription
    async def subscribe_dm(self, receiver_id: int, sender_id: int) -> AsyncGenerator[Optional[DirectMessage], None]:
        while True:
            message = await direct_message_subscriptions.get()
            if message.receiver_id == receiver_id and message.sender_id == sender_id:
                yield message


class DirectMessageSubscriptionBroker:
    def __init__(self):
        # NOTE Production 実装では Redis などの PubSub システムを利用する
        self._queue = asyncio.Queue()
    
    async def publish(self, dm: DirectMessage):
        await self._queue.put(dm)
    
    async def get(self):
        return await self._queue.get()


direct_message_subscriptions = DirectMessageSubscriptionBroker()
