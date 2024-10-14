#!/usr/bin/env python3
"""
Module for zooming an array using type annotations and mypy checks.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    where each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples, with sequence and length.
    """
    return [(i, len(i)) for i in lst]
