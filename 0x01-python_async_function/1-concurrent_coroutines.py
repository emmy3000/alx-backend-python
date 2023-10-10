#!/usr/bin/env python3
'''
Asynchronous coroutines for generating random delays
and executing multiple coroutines concurrently.
'''
import asyncio
import random
from typing import List, Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    '''
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive).

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay.
    '''
    if max_delay < 0:
        raise ValueError("max_delay must be a non-negative number")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: Union[int, float] = 10) -> List[float]:
    '''
    Execute the wait_random coroutine n times concurrently
    with the specified max_delay.

    Args:
        n (int): The number of times to execute wait_random concurrently.
        max_delay (Union[int, float]): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        List[float]: A list of the delays in ascending order.
    '''
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Create a list to store the delays
    delays = []

    # Create a list of tasks for concurrent execution
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
