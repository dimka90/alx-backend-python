#!/usr/bin/env python3

"""
A coroutine that will execute async_comprehension four times in
parallel using asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    A function that executes in parallel
    """
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    time_end = time.perf_counter()
    return time_end - start_time
