#!/usr/bin/env python3
"""
This module defines a function task_wait_random which
returns an asyncio.Task.
"""

import asyncio
import importlib.util
spec = importlib.util.spec_from_file_location("wait_random", "./0-basic_async_syntax.py")
wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random)


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that runs wait_random.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.
    
    Returns:
        asyncio.Task: A task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
