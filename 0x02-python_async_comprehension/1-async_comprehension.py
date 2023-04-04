#!/usr/bin/env python3
'''Async comprehension'''
from typing import List
import async_generator
__import__(0-async_generator)

async_generator = 0-async_generator.async_generator


async def async_comprehension() -> List[float]:
    '''Creating a list of 10 numbers'''
    return [num async for num in async_generator()]
