#!/usr/bin/env python3
'''basic asyncio syntax'''
import asyncio
import random


async def wait_random(max_delay: int = 10.0) -> float:
    '''Executes basic asyncio task that waits for random time'''
    wait = random.random()*max_delay
    await asyncio.sleep(wait)
    return wait
