#!/usr/bin/env python3

"""
This module defines a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the result of multiplying it by the multiplier.
    """

    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the provided multiplier.

        Args:
            x (float): The input float to be multiplied.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
