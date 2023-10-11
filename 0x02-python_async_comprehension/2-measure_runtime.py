#!/usr/bin/env python3
'''
Measure Runtime

This module defines a function for measuring the runtime
of parallel asynchronous comprehensions.
'''
import asyncio
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime for running four parallel asynchronous comprehensions.

    Returns:
        float: The total runtime for running the comprehensions.
    '''
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
