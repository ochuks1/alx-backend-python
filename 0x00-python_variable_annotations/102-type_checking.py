#!/usr/bin/env python3
"""
Module for zooming an array with type annotations and mypy checks.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Zooms in on an array by duplicating its elements.

    Args:
        lst (Tuple[int, ...]): The input tuple whose elements are to be duplicated.
        factor (int): The number of times to duplicate each element.

    Returns:
        List[int]: A list containing the zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
