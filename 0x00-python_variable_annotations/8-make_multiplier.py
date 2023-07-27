#!/usr/bin/env python3
'''Multiplier module
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Multiplies float by multiplier
    '''
    return lambda m: m * multiplier
