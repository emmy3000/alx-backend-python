#!/usr/bin/env python3

"""
This module defines a function to calculate the sum of floats in a list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of floats in a list.

    Args:
        input_list (List[float]): The list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
