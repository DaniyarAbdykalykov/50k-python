from typing import Union

def mysum(lst: Union[list, tuple]):
    n = 0
    for i in lst:
        n += i
    return n