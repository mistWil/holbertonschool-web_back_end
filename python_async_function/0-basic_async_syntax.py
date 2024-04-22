#!/user/bin/python3


"""The basics of async"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire entre 0 et max_delay secondes,
    puis renvoie ce délai.

    Args:
        max_delay (int, optional): Délai maximum en secondes. Défaut est 10.

    Returns:
        float: Délai aléatoire en secondes.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
