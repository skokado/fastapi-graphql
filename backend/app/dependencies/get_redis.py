from typing import AsyncGenerator

import redis.asyncio as redis

from app.config.db import REDIS_URL


async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    conn = redis.from_url(REDIS_URL)
    try:
        yield conn
    finally:
        await conn.close()
