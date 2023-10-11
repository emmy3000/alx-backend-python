# !/usr/bin/env python3
"""
Create asyncio.Tasks for the wait_random coroutine
multiple times concurrently.
"""
import asyncio
from typing import List

# Import 'task_wait_random' from '3-tasks'
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for the wait_random coroutine n times concurrently
    with the specified max_delay.

    Args:
        n (int): The number of times to execute wait_random concurrently.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
