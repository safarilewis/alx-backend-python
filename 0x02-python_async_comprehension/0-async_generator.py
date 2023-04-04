#!/usr/bin/env python3
"""Asynchronous coroutine"""

import random
from typing import Generator
import asyncio

async def async_generator()->Generator[float, None, None]:
    '''Generating a sequence of ten numbers'''
    for int in range(10):
        await asyncio.sleep(1)
        return random.random()

