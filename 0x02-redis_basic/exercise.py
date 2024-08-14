#!/usr/bin/env python3
"""
Module for Cache class
"""


from typing import Any
import redis
import uuid


class Cache:
    """ Class for writing strings to Redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Generates a random key, store data in Redis using the random key
        return the key
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
