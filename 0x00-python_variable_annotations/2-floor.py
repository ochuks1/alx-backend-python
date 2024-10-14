#!/usr/bin/env python3
import math
"""
This module contains a function that returns the floor of a float.
"""


def floor(n: float) -> int:
    """Returns the floor of the float.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The largest integer less than or equal to the float.
    """
    return math.floor(n)
