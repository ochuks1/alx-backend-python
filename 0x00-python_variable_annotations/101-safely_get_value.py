#!/usr/bin/env python3
"""
This module defines a function safely_get_value.
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Get the value from the dictionary for a given key.

    Args:
        dct (Mapping): The dictionary to search.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The value to return if the key is not found.

    Returns:
        Union[Any, T]: The value for the key if it exists, otherwise default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
