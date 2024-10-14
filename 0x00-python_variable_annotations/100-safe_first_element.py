#!/usr/bin/env python3
"""
This module defines a function safe_first_element.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence, or None if empty.

    Args:
        lst (Sequence[Any]): A sequence to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of a sequence, or None if empty.
    """
    if lst:
        return lst[0]
    return None
