#!/bin/bash env python3

import asyncio
import random

async def wait_random(max_delay=10.0):
    await asyncio.sleep(random.random(0.0,max_delay))
    print(max_delay)
