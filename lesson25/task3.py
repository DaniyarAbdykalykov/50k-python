def foo(*args):
    fist, *middle, last = args
    return fist, middle, last

print(foo(1, 2, 3, 4, 5))
print(foo('a', 'b', 'c'))
