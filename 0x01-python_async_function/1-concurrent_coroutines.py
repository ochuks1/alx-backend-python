#!/usr/bin/env python3
"""
A module that contains a coroutine to wait for random delays.
"""
import asyncio
from wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Executes wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for wait_random.
    
    Returns:
        list: A sorted list of delays.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delays  # Return the delays as is for now
