#!/usr/bin/env python3

"""
This script defines a function to zoom in on an array.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zoom in on an array by repeating its elements.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple: The zoomed-in tuple.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)
