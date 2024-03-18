#!/usr/bin/env python3

"""
This program use runs program concurently using the asyncio module
"""
import asyncio
wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    A function that returns a list of asyn random calls
    Arguments:
            n: number of ilteration
            max_delay: number of time delay period

    Return:
            A list of sorted random generated numbers
    """

    tasks = [wait(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    return sorted(delays)
