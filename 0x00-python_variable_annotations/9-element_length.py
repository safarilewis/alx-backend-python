#!/usr/bin/env python3
'''Let's duck type an iterable object
'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence[int]]]:
    '''Computes the length of a List
    '''
    return [(i, len(i)) for i in lst]
