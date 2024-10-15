#!/usr/bin/env python3
"""
This module defines a function measure_time that calculates
the average execution time for wait_n.
"""

import time
import asyncio
from 1_concurrent_coroutines import wait_n


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
