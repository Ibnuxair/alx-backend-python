#!/usr/bin/env python3
""" Multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
