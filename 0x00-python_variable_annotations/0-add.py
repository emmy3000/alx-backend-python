#!/usr/bin/python3

"""
The script demostrates a simple addition function
utilizing variable type annotation syntax.
"""


def add(a: float, b: float) -> float:
    """
    Calculate the sum of two floating-point numbers.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of 'a' and 'b' as a floating-point number.
    """
    return a + b
