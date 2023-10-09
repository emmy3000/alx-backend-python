#!/usr/bin/env python3

"""
This script defines a function to calculate the length
of elements in an iterable.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing elements
        from the input iterable and their lengths.
    """
    return [(i, len(i)) for i in lst]
