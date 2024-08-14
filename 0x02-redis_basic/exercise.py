#!/usr/bin/env python3
"""
Module for Cache class
"""

from typing import Callable, Union, Optional
import redis
import uuid


class Cache:
    """ Class for writing strings to Redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @functools.wraps
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, store data in Redis using the random key
        return the key
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, None]:
        """
        Retrieve data from Redis and apply a conversion function
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis, decoded from bytes
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis
        """
        return self.get(key, fn=int)
