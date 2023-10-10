#!/usr/bin/env python3
'''
Create an asyncio.Task for the wait_random coroutine
with the given max_delay.
'''
import asyncio

# Import wait_random from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''
    Create an asyncio.Task for the wait_random coroutine
    with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.
    '''
    return asyncio.create_task(wait_random(max_delay))


async def test(max_delay: int):
    '''
    Test the task_wait_random function by creating an asyncio.
    Future with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.
    '''
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
