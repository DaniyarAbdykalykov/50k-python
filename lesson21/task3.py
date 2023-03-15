from typing import Union

def mymax(lst: Union[list, tuple]):
    for i in range(len(lst)):
        m = i
        for j in range(len(lst)):
            if lst[j] > lst[m]:
                m = j
        return lst[m]