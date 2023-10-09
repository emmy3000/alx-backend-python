#!/usr/bin/env python3

"""
This module defines a function to safely retrieve a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

# Create a `TypeVar` for the return type to save the relationship btw key
# and default
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve from the dictionary.
        default (Union[T, None], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
        or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
