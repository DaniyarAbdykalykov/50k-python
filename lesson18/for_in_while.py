m = [5, 2, 5, 3, 7, 4, 3, 1, 4, 6]
k = []

while m:
    c = m[0]
    for e in m:
        if c > e:
            c = e
    k.append(c)
    m.remove(c)

print(k)