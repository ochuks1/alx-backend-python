#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine `wait_n`,
which spawns `wait_random` n times with a specified max_delay.
The results are returned as a list of delays in ascending order.
"""

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with a specified max_delay and
    returns the list of delays in ascending order without using sort().
    
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
