#!/usr/bin/env python3
"""
Module for zooming an array with type annotations and mypy checks.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom an array by repeating each element by a given factor.

    Args:
        lst (Tuple[int, ...]): The tuple of integers.
        factor (int, optional): The repetition factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
