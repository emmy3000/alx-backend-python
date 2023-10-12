#!/usr/bin/env python3
"""
Measure the runtime of wait_n coroutine.
"""
import time
import asyncio
import random
from typing import List, Union

# Import the entire module and then access its wait_n method
concurrent_coroutines = __import__('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive).

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay.
    """
    if max_delay < 0:
        raise ValueError("max_delay must be a non-negative number")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average execution time for wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
