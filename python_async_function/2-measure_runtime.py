#!/usr/bin/python3


"""Measure the runtime"""


import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n_1 = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total pour wait_n(n, max_delay) et renvoie
    le temps moyen par appel de wait_n.

    Args:
        n (int): Nombre de fois à exécuter wait_n.
        max_delay (int): Délai maximum en secondes pour wait_n.

    Returns:
        float: Temps moyen d'exécution de wait_n en secondes.
    """
    start_time = time.time()
    asyncio.run(wait_n_1(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
