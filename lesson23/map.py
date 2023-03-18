def test(n):
    return n * 2

a = [3, 2, 4, 23]

b = [e * 2 for e in a]
print(b)

c = list(map(lambda x : x*2, a))
print(c)


d = list(map(test, a))
print(d)