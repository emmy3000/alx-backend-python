# !/usr/bin/env python3
'''
Create asyncio.Tasks for the wait_random coroutine
multiple times concurrently.
'''
import asyncio
from typing import List, Union

# Import wait_random from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: Union[int, float]) -> List[float]:
    '''
    Create asyncio.Tasks for the wait_random coroutine n times concurrently
    with the specified max_delay.

    Args:
        n (int): The number of times to execute wait_random concurrently.
        max_delay (Union[int, float]): The maximum delay in seconds.

    Returns:
        List[float]: A list of the delays in ascending order.
    '''
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
