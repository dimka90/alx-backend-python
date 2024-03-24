#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes a
float multiplier as argumentand returns a function that
"""

from typing import FloatFunction


def make_multiplier(multiplier: float) -> FloatFunction:
    """
    This function takes a float multiplier and returns a new function
    that multiplies a float by the given multiplier.
    Args:
      multiplier: The float value to be used for multiplication.

    Returns:
      A function that takes a float and returns its product
      with the multiplier.
    """
    def inner(number: float) -> float:
        """
        This inner function multiplies a float by the multiplier.
        Args:
            number: The float to be multiplied.
        Returns:
        The product of the number and the multiplier.
        """
        return number * multiplier
    return inner
