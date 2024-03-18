#!/usr/bin/env python3
"""
Generate a new element in Redis
"""
import redis
from typing import Callable, Optional, Union
from uuid import uuid4, UUID


class Cache:
    """ Class for implementing a Cache """

    def __init__(self):
        """ Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a
        random key and return the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
    
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        store input data in dedis using a random key
        and return a key
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        param a value from redis to str
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: int) -> int:
        """
        param a value from redis to int
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
    
