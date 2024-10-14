#!/usr/bin/env python3
"""
Module for returning functions by float.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float as a multiplier and returns a function that multiplies
    a float by this multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the input and the multiplier.
    """
    return lambda x: x * multiplier
