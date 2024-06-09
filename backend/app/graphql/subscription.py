import asyncio
import dataclasses
from datetime import datetime
import json
from typing import AsyncGenerator

import redis.asyncio as redis
import strawberry

from app.resolvers.direct_message import get_latest_message

from .schemas import DirectMessage


async def count_resolver(target: int = 10) -> AsyncGenerator[int, None]:
    for i in range(1, target + 1):
        yield i
        await asyncio.sleep(0.5)


@strawberry.type
class Subscription:
    count = strawberry.subscription(resolver=count_resolver)

    @strawberry.subscription
    async def subscribe_dm(self, receiver_id: int, sender_id: int, info: strawberry.Info) -> AsyncGenerator[DirectMessage, None]:
        last_message = await get_latest_message(receiver_id, sender_id, info.context.db)
        if last_message:
            yield last_message

        async for message in direct_message_subscriptions.subscribe(info.context.redis, last_message.id):
            data = json.loads(message["data"])
            dm = DirectMessage(**data)
            dm.created_at = datetime.fromisoformat(dm.created_at)
            yield dm


class DirectMessageSubscriptionBroker:
    channel = "channel:DirectMessage"

    async def publish(self, dm: DirectMessage, redis: redis.Redis):
        dm.created_at = dm.created_at.isoformat()
        payload = json.dumps(dataclasses.asdict(dm))
        await redis.publish(self.channel, payload)
    
    async def subscribe(self, redis: redis.Redis, last_id: int = 0) -> dict:
        pubsub = redis.pubsub()
        await pubsub.subscribe(self.channel)
        async for message in pubsub.listen():
            if message["type"] != "message":
                continue
            yield message


direct_message_subscriptions = DirectMessageSubscriptionBroker()
