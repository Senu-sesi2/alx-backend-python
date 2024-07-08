#!/usr/bin/env python3
""" Measure the runtime """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time it takes to run `wait_n` with `n` coroutines
    that wait for random amounts of time up to `max_delay` seconds.
    Returns the average time taken per coroutine.
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_out = time.perf_counter() - s
    return time_out / n
