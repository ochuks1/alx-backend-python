#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary with type annotations.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary by key, or return a default value if the key does not exist.

    Args:
        dct (Mapping[Any, Any]): The dictionary to retrieve the value from.
        key (Any): The key to search for.
        default (Union[T, None], optional): The default value if the key is not found.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

