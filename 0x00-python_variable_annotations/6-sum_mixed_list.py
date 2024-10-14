#!/usr/bin/env python3
"""
Module for getting string representation of a list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns the sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
        float: The sum of all numbers in the list as a float.
    """
    return float(sum(mxd_lst))
