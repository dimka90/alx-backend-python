#!/usr/bin/env python3
"""
A program a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function calculate the all the element in a list
    Arguments:
            mxd_list: List of element both integers and float

    Return:
            Sum of all the numbers in the list
    """
    sum: float = 0.0

    for i in mxd_lst:
        sum = sum + i
    return sum
