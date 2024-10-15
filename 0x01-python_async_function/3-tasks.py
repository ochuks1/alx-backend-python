#!/usr/bin/env python3
"""
A module that contains a function to create an asyncio Task
from wait_random.
"""
import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task from the wait_random coroutine.
    
    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.
    
    Returns:
        asyncio.Task: The task created from wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
