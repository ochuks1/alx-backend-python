#!/usr/bin/env python3
"""
A module that contains a function to wait for random delays using tasks.
"""
import asyncio
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay value for the tasks.
    
    Returns:
        list: A list of delays returned by the tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays  # The delays will be returned as is
