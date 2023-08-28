#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
import random
import asyncio
from typing import List
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns a asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
