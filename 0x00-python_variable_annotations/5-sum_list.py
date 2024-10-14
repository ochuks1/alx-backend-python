#!/usr/bin/env python3
"""
Module for working with a list of floats.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats and return the result.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
