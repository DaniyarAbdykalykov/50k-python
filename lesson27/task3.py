def iteration(a: str | list | tuple):
    if isinstance(a, int):
        raise TypeError("Число не является итерируемым объектом")
    elif isinstance(a, dict):
        raise TypeError("Функция принимает только строки, списки, кортежи")
    elif isinstance(a, float):
        raise TypeError("Число не является итерируемым объектом")
    elif isinstance(a, set):
        raise TypeError("Функция принимает только строки, списки, кортежи")
    elif isinstance(a, frozenset):
        raise TypeError("Функция принимает только строки, списки, кортежи")
    else:
        for e in a:
            print(e)