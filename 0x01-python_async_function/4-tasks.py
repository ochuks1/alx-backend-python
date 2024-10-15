#!/usr/bin/env python3
"""
Function to create multiple asyncio tasks for wait_random.
"""
from typing import List
import asyncio
import importlib.util
spec = importlib.util.spec_from_file_location("task_wait_random", "./3-tasks.py")
task_wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_wait_random)
task_wait_random = task_wait_random_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]
    """
    Executes task_wait_random n times and returns a list of delays.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random.task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
