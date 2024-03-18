#!/usr/bin/env python3

"""
This program uses asyncio module in python to generate random value
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    An async function that returns a random number as float
    Arguments:
            max_delay: maximum number to be generated the random function
    Return:
            The random generated value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
