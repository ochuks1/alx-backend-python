#!/usr/bin/env python3
"""
This module defines a measure_time function to compute the average time
it takes for wait_n to execute.
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
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    
    return total_time / n
