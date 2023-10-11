#!/usr/bin/env python3
"""
Async Generator

This module defines an asynchronous generator coroutine that yields
random numbers between 0 and 10 after waiting for 1 second in each
iteration.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    '''
    Asynchronous generator that yields random integers.

    Yields:
        int: Random integers between 0 and 10.

    Delays:
        1 second between each yield.

    Returns:
        Generator[int, None, None]: An asynchronous generator.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
