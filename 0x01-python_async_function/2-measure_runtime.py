#!/usr/bin/env python3
"""
This module defines a function measure_time that calculates
the average execution time for wait_n.
"""

import time
import importlib.util
import asyncio

spec = importlib.util.spec_from_file_location("wait_n", "./1-concurrent_coroutines.py")
wait_n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_n)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns
    the average time per coroutine.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay for each coroutine.
    
    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
