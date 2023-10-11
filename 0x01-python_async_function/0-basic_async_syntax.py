#!/usr/bin/env python3
'''
Asynchronous coroutine for generating random delays.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay.
    '''
    if max_delay < 0:
        raise ValueError("max_delay must be a non-negative number")

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
