def mymult(a, b):
    if isinstance(a, str) and isinstance(b, str):
        raise TypeError("Нельзя умножать строку со строкой")
    elif isinstance(a, set) and isinstance(b, set):
        raise TypeError("Нельзя умножать множество на множество")
    elif isinstance(a, int) and isinstance(b, set) or isinstance(a, set) and isinstance(b, int):
        raise TypeError('Нельзя умножать число с множеством')
    elif isinstance(a, int) and isinstance(b, tuple) or isinstance(a, tuple) and isinstance(b, int):
        raise TypeError("Нельзя умножать число с кортежом")
    elif isinstance (a, tuple) and isinstance(b, tuple):
        raise TypeError("Нельзя кортеж умножать на кортеж")
    elif isinstance (a, list) and isinstance(b, list):
        raise TypeError("Нельзя список умножать на список")
    elif isinstance(a, int) and isinstance(b, list) or isinstance(a, list) and isinstance(b, int):
        raise TypeError("Нельзя умножать число на список")
    elif isinstance(a, dict) and isinstance(b, dict):
        raise TypeError("Нельзя умножать словарь на словарь")
    elif isinstance(a, int) and isinstance(b, dict) or isinstance(a, dict) and isinstance(b, int):
        raise TypeError("Нельзя умножать число на словарь")
    elif isinstance(a, frozenset) and isinstance(b, frozenset):
        raise TypeError("Нельзя умножать неизменяемое множество с неизменяемым множеством")
    elif isinstance(a, int) and isinstance(b, frozenset) or isinstance(a, frozenset) and isinstance(b, int):
        raise TypeError("Нельзя умножать число с неизменяемым множеством")

    return a * b


print(mymult(2, 5))
print(mymult("qwerty", 2))

print(mymult((1, 2, 2, 3), 2))