#!/usr/bin/env python3
"""
to_kv that takes a string k and an int OR float
v as arguments and returns a tuple. The first
element of the tuple is the string k. The second
element is the square of the int/floatv and should
be annotated as a float.
"""

from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    A function that takes a str and either a float or an int
    and return the str, raising the int / float to by exponent
    of two
    Arguments:
            k: String
            v: int/float to raise to exponent of 2
    Returns:
            Tuple containing a str and the result of the int/float by
            raised to the power of two
    """

    return (k, v ** 2)
