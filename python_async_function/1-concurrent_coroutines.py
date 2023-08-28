#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
import random
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time with async"""
    coros = [wait_random(max_delay) for i in range(n)]

    list_num = await asyncio.gather(*coros)
    return sorted(list_num)
