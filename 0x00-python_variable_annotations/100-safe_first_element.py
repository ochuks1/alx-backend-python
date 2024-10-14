#!/usr/bin/env python3
"""
This module defines a function safely_get_value.
"""

from typing import Mapping, Any, Optional, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    return default
