#!/usr/bin/env python3
""" async_generator function """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yield a random number between 0 and 10 """

    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
