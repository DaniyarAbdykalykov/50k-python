add = lambda a, b, c, d: a + b + c + d

multiply = lambda a, b, c, d: a * b * c * d

more = lambda a, b, c: True if a > b and a > c else False

equal = lambda a, b, c: True if a == b == c else False

print(add(1, 2, 3, 4))
print(multiply(1, 2, 3, 4))
print(more(5, 4, 3))
print(equal(4, 4, 4))