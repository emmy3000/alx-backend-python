#!/usr/bin/env python3

"""
This module defines a function to create a tuple from a string
and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int or float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple containing the input string
        and the square of the input int or float.
    """
    return (k, v ** 2)
