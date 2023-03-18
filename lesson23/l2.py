def multiplier(n):
    return lambda k: k * n


doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(6))
print(tripler(6))