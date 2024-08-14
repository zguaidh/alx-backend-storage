#!/usr/bin/env python3
"""
Module for Cache class
"""

from typing import Callable, Union, Optional
import redis
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called
    """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores the history of inputs and outputs
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper


@staticmethod
def replay(method: Callable):
    """
    Display the history of calls to a particular function.
    """
    r = redis.Redis()
    value = r.get(function_name)
    value = int(value.decode("utf-8"))
    method_name = method.__qualname__
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)
    for inp, out in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        out = out.decode("utf-8")
        print(f"{method.__qualname__}(*{inp}) -> {out}")


class Cache:
    """ Class for writing strings to Redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, store data in Redis using the random key
        return the key
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, None]:
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
        Retrieve a str from Redis, decoded from bytes
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an int from Redis
        """
        return self.get(key, fn=int)
