#!/usr/bin/env python3
"""
Module for getting string representation of a list.
"""

from typing import List

def to_str_list(input_list: List[int]) -> List[str]:
    """
    Convert a list of integers into a list of strings.

    Args:
        input_list (List[int]): A list of integers.

    Returns:
        List[str]: A list of the integers as strings.
    """
    return [str(i) for i in input_list]

