#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine, `wait_random`,
which waits for a random delay between 0 and `max_delay` seconds
before returning the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay to wait for (default is 10).

    Returns:
        float: The actual delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
