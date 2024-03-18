#!/usr/bin/env python3
"""Generate a new element in Redis"""
import redis
from typing import Union
from uuid import uuid4, UUID


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
        """Store the input data in Redis using a
        random key and return the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
