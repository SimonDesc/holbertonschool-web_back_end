#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather"""
    start_time = time.time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time
