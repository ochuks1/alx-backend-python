#!/usr/bin/env python3
"""
Zooms in on each element of the input tuple by a specified factor.

Args:
    lst (Tuple): A tuple of elements to zoom in on.
    factor (int): The factor by which to zoom in. Defaults to 2.

Returns:
    List: A list of elements zoomed in by the specified factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list of elements zoomed in by the specified factor."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
