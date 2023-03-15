def mypow(number: int, power: int):
    equal = 1
    for i in range(power):
        equal *= number
    return equal