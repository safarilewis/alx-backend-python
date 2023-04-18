#!/usr/bin/env python3
'''Async comprehension task'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creating a list of 10 numbers'''
    return [x async for x in async_generator()]
