#!/usr/bin/env python3
"""
This module defines a function safe_first_element.

safe_first_element(lst: Sequence) -> Union[Any, None]:
    Returns the first element of a sequence or None if the sequence is empty.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if available, otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: The first element of the sequence or None if empty.
    """
    if lst:
        return lst[0]
    else:
        return None
