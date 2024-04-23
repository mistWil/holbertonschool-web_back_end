#!/usr/bin/env python3

"""Task 4"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute n fois la coroutine task_wait_random
    avec un délai maximum de max_delay,
    et renvoie la liste des délais obtenus dans l'ordre croissant.

    Args:
        n (int): Nombre de fois à exécuter task_wait_random.
        max_delay (int): Délai maximum en secondes pour task_wait_random.

    Returns:
        List[float]: Liste des délais obtenus, dans l'ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
