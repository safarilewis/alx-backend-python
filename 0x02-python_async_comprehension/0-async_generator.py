#!/usr/bin/env python3
"""Asynchronous coroutine"""

import random
from typing import Generator
import asyncio

async def async_generator()->Generator[float, None, None]:
    '''Generating a sequence of ten numbers'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()*10
