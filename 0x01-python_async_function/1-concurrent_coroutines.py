#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''
from typing import List
import asyncio

wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes n times'''
    n_times = await asyncio.gather(
        *tuple(map(lambda _: wait(max_delay), range(n)))
    )
    sorted_times = sorted(n_times)
    return sorted_times
