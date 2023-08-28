#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
import random
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time with async"""
    coros = [task_wait_random(max_delay) for i in range(n)]

    list_num = await asyncio.gather(*coros)
    return sorted(list_num)
