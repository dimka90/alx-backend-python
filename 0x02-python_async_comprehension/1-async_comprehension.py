#!/usr/bin/env python3

"""
A coroutine that will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This functions call the async_generator function
    Argument:
            None
    Return:
            A list of numbers
    """

    return [_ async for _ in async_generator()]
