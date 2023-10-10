# 0x01. Python - Async

Welcome to the documentation for Python asynchronous programming using the `async` and `await` syntax along with the `asyncio` library. This guide will cover the basics of asynchronous programming, working with concurrent coroutines, asyncio tasks, and using the `random` module effectively.

## Table of Contents

- [Async and Await Syntax](#async-and-await-syntax)
- [Executing an Async Program with asyncio](#executing-an-async-program-with-asyncio)
- [Running Concurrent Coroutines](#running-concurrent-coroutines)
- [Creating asyncio Tasks](#creating-asyncio-tasks)
- [Using the Random Module](#using-the-random-module)

## Async and Await Syntax

Asynchronous programming in Python allows you to write non-blocking code efficiently handling I/O-bound operations. Key elements include:

- `async`: Used to define asynchronous functions that can pause their execution, allowing other tasks to run concurrently.
- `await`: Used inside an async function to pause execution until the awaited coroutine or future is completed.

```python
import asyncio

async def async_function():
    result = await some_coroutine()
    # Rest of the code
```

## Executing an Async Program with asyncio

- To run an `async` program, utilize the `asyncio` library as shown in the following example:
```python
import asyncio

async def main():
    await asyncio.gather(coroutine1(), coroutine2())

asyncio.run(main())
```
- `asyncio.run(main())` function executes the `main()` coroutine and manages the event loop.

## Running Concurrent Coroutines

`asyncio.gather()` enables running multiple coroutines concurrently:
```python
async def main():
    await asyncio.gather(coroutine1(), coroutine2())
```

## Creating asyncio Tasks

Use `asyncio.create_task()` to create tasks from coroutines:
```python
async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await task1
    await task2
```

## Using the Random Module

The `random` module provides functions for generating random numbers:
```python
import random

random_number = random.randint(1, 100)
```

You can use these random numbers in your async programs as needed.

This README documentation offers a concise overview of asynchronous programming in Python, covering syntax, execution, concurrency, and the usage of the `random` module. Utilize these concepts to write efficient and responsive async code in Python.



