#!/user/bin/python3


"""Tasks"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio qui exécute wait_random
    avec le délai maximum spécifié.

    Args:
        max_delay (int): Délai maximum en secondes pour wait_random.

    Returns:
        asyncio.Task: Tâche asyncio qui exécute wait_random.
    """
    coroutine = wait_random(max_delay)

    # Créer une tâche asyncio qui exécute la coroutine
    task = asyncio.create_task(coroutine)

    # Renvoyer la tâche asyncio
    return task
