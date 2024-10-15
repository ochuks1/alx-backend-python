#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension.

This module measures the total execution time of the
async_comprehension function executed four times in parallel.
"""

import asyncio
import time
import importlib

async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of async_comprehension executed 4 times.

    Returns:
        float: The total runtime.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.time() - start_time
