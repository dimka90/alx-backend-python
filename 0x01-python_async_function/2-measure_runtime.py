#!/usr/bin/env python3

"""
A program that calculate the time taken for a program to run
"""

import asyncio
import time
wait = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the time elasped of async program
    Arguments:
            n: number of process to spwan
            max_delay: time to delay
    Return:
          A float representing the time dealy
    """
    # Record time start
    start_time = time.perf_counter()
    asyncio.run(wait(n, max_delay))
    # Record when time stop
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
