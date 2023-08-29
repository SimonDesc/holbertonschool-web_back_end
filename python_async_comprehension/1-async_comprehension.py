#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """yield a random number between 0 and 10"""

    return [i async for i in async_generator()]
