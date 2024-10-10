#!/usr/bin/env python3
"""
Module for working with a list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list containing both integers and floats and return the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the list as a float.
    """
    return sum(mxd_lst)

