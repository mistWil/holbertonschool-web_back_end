#!/user/bin/python3


""" Let's duck type an iterable object"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """9-element_length"""
    return [(i, len(i)) for i in lst]
