#!/user/bin/python3


"""Async Comprehensions"""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collecte 10 nombres aléatoires en utilisant une async
    comprehension sur async_generator.
    """
    return [i async for i in async_generator()]
