def mypow(number: int, power: int):
    equal = 1
    for i in range(0, power):
        equal *= number
    return equal