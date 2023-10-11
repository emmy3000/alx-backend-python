#!/usr/bin/env python3
'''
Create an asyncio.Task for the wait_random coroutine
with the given max_delay.
'''
import asyncio

# Import wait_random from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Create an asyncio.Task for the wait_random coroutine
    with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        async.Task: An asyncio task that waits for a random delay.
    '''
    random_delay_task = asyncio.create_task(wait_random(max_delay))
    return random_delay_task
