#!/bin/bash/env python3
'''basic asyncio syntax'''
import asyncio
import random


async def wait_random(max_delay=10.0):
    wait = random.random()*max_delay
    await asyncio.sleep(wait)
    return wait
