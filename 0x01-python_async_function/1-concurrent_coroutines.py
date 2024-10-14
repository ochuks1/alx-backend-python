#!/usr/bin/env python3
import asyncio
from typing import List
from wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of all delays in ascending order.
    """
    delays = []

    # Create a list of tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    for delay in await asyncio.gather(*tasks):
        # Insert each delay in the correct position to maintain sorted order
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)  # Insert the delay at the correct position

    return delays
