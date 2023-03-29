def iteration(a: str | list | tuple):
    try:
        for e in a:
            print(e)
    except TypeError:
        print("Функция принимает только строки, списки, кортежи")