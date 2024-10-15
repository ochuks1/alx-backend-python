#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine `wait_n` that spawns
the `wait_random` coroutine n times with a specified max_delay and 
returns the list of delays in ascending order.
"""

import asyncio
from typing import List
import importlib.util

spec = importlib.util.spec_from_file_location("wait_random", "./0-basic_async_syntax.py")
wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay and returns
    a list of all delays in ascending order without using sort().

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.
    
    Returns:
        List[float]: List of delays sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
