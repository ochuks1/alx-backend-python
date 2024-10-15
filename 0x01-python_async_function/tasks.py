#!/usr/bin/env python3
"""
This module defines a function task_wait_random which
returns an asyncio.Task.
"""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that runs wait_random.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.
    
    Returns:
        asyncio.Task: A task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
