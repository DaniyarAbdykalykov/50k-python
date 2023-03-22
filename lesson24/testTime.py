import time

def testTime(fn):
    def wrapper(*args, **kwarqs):
        st = time.time()
        res = fn(*args, **kwarqs)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
        return res
    return wrapper

@testTime
def getNOD(a, b):
    while a != b:
        if a > b: a -=b
        else: b -= a
    return a

@testTime
def getFastNOD(a, b):
    if a < b: a,b = b,a
    while b: a,b = b, a%b
    return a


res = getNOD(100000, 2)
print(res)
# getFastNOD(100000, 2)
# test1 = testTime(getNOD)
# test2 = testTime(getFastNOD)
# test1(100000, 2)
# test2(100000, 2)

