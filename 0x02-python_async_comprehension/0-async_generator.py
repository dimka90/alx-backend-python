#!/usr/bin/env python3

"""
Creates a generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    Argument:
        None
    Return:
        A range pf numbers
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
