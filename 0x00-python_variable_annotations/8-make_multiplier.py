#!/usr/bin/env python3
"""
Module for getting a value from a dictionary safely.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Get a value from a dictionary if the key exists, otherwise return the default value.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

