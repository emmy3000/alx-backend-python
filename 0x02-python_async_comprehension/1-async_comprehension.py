#!/usr/bin/env python3
"""
Async Comprehension

This module defines an asynchronous comprehension function
that generatesa list of random numbers between 0 and 10.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension function generates
    a list of random numbers between 0 and 10
    using an imported async generator function.

    Returns:
        List[float]: A list of random numbers between 0 and 10.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
