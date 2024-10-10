#!/usr/bin/env python3
"""
Module for getting the first element of a sequence with duck typing.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a sequence, or return None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: The first element or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

