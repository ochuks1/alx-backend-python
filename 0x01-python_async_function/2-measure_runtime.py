#!/usr/bin/env python3
"""
A module to measure the execution time of wait_n.
"""
import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).
    
    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for wait_random.
    
    Returns:
        float: The average time taken for each wait_random call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    return total_time / n
