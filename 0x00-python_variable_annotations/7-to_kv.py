#!/usr/bin/env python3
"""
Module for getting the first element of a sequence with duck typing.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, and returns a tuple.

    Args:
        k (str): The string.
        v (Union[int, float]): An integer or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string, 
        and the second element is the square of the int/float as a float.
    """
    return (k, float(v ** 2))
