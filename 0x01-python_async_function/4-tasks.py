#!/usr/bin/env python3
'''Task 4 file'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''runs task wait rand n times'''
    times = await asyncio.gather(*tuple(map(lambda _: task_wait_random(max_delay), range(n))))
    sorted_times = sorted(times)
    return sorted_times
