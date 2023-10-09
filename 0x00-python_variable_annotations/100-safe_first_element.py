#!/usr/bin/env python3

"""
This module defines a function to safely retrieve
the first element of an iterable.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieve the first element of an iterable.

    Args:
        lst (Sequence): The input iterable.

    Returns:
        Union[Any, NoneType]: The first element if it exists,
        or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
