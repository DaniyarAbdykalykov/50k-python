def mymult(a, b):
    if isinstance(a, str) and isinstance(b, str):
        raise TypeError("Нельзя умножить строку со строкой")
    elif isinstance(a, set) and isinstance(b, set):
        raise TypeError("Нельзя умножить множество на множество")
    elif isinstance(a, int) and isinstance(b, set):
        raise TypeError('Нельзя умножить число с множеством')

    return a * b

num_1 = int(input())
num_2 = int(input())

print(mymult(num_1, num_2))
     