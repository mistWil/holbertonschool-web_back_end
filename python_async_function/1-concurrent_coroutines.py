#!/usr/bin/python3


"""Execute multiple coroutines at the same time with async"""


import asyncio
from typing import List
import sys
import importlib
sys.path.insert(
    0, '/home/mist_wil/holbertonschool-web_back_end/python_async_function')
basic_async_syntax = importlib.import_module('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute n fois la coroutine wait_random avec un délai maximum de max_delay,
    et renvoie la liste des délais obtenus dans l'ordre croissant.

    Args:
        n (int): Nombre de fois à exécuter wait_random.
        max_delay (int): Délai maximum en secondes pour wait_random.

    Returns:
        List[float]: Liste des délais obtenus, dans l'ordre croissant.
    """
    coroutines = (basic_async_syntax.wait_random(max_delay) for _ in range(n))
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
