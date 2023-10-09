#!/usr/bin/env python3

"""
This module defines a function to calculate the sum of integers and floats
in a mixed list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the numbers in the mixed list as a float.
    """
    return sum(mxd_lst)
