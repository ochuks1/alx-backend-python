#!/usr/bin/env python3
"""
This module defines a function task_wait_n that spawns
task_wait_random n times and returns the list of delays
in ascending order.
"""

import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with max_delay and returns
    a list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.
    
    Returns:
        List[float]: List of delays sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    
    return delays
