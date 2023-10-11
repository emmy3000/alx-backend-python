#!/usr/bin/env python3
"""
Asynchronous coroutines for generating random delays
and executing multiple coroutines concurrently.
"""
import asyncio
from typing import List
import random

# Import coroutines function from '0-basic_async_syntax'
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine that generates random delays and
    executes multiple coroutines concurrently.

    Args:
        n (int): The number of times to execute the coroutine concurrently.
        max_delay (int, optional): The maximum delay in seconds (inclusive).
            Defaults to 10.

    Returns:
        List[float]: A list of random delays in ascending order.
    Raises:
        ValueError: If 'n' is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    results = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        results.append(delay)

    return results
