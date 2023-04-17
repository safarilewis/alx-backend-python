#!/usr/bin/env python3
'''Measure run time'''
import asyncio
import time


n_times = __import__('1-concurrent_coroutines').n_times


def measure_time(n: int, max_delay: int) -> float:
    '''measures the runtime of the asyncio task '''
    start = time.time()
    asyncio.run(n_times(n, max_delay))
    return (time.time()-start)/n
