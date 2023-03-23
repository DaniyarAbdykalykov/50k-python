def mysum(r, *args, l):
    for num in args:
        r += num
    return r, l

print(mysum(3, 5, 3, 0, 1))