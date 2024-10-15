#!/usr/bin/env python3
"""
Async comprehension that collects random numbers.

This module imports async_generator and uses it to collect 10 random
numbers via async comprehension.
"""

from typing import List
import importlib

async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]
