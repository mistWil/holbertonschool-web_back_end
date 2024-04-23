#!/usr/bin/env python3


"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
