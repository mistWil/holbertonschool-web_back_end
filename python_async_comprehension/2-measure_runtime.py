#!/usr/bin/env python3


"""Run time for four parallel comprehensions"""


import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension quatre fois en parallèle et
    mesure le temps total d'exécution.

    Returns:
        float: Temps total d'exécution en secondes.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
