#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
import random
import asyncio
from typing import List
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the delay"""

    async def _internal_mesure():
        start_time = time.time()

        await wait_n(n, max_delay)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return elapsed_time

    return asyncio.run(_internal_mesure())
