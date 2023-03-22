def composition(f, g):
    def inner(*args, **kwargs):
        return f(g(*args, **kwargs))
    return inner



h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))

h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))

h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))

