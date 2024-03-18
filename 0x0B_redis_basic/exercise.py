#!/usr/bin/env python3
"""Generate a new element in Redis"""
import redis
from typing import Union
import uuid


class Cache:
    """
    This Python class `Cache` initializes a Redis connection and
    provides a method `store` to store data
    in Redis with a generated UUID key.
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database: clear old entries

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """Store the data with a uuid key"""
        uuid_key = uuid.uuid4()
        uuid_key = str(uuid_key)
        if not data:
            return uuid_key

        self._redis.set(uuid_key, data)
        return uuid_key
