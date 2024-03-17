#!/usr/bin/env python3

"""
This program takes in a list of numbers and return there sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function calculate the sum of all the floating points numbers

    Argument:
            input_list: A floating array of list
    Return:
          float: sum of the elements in the list
    """

    sum: float = 0.0
    for i in input_list:
        sum = sum + i
    return sum
