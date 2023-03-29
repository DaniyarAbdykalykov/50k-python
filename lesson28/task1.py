def mymult(a, b):
    try:
        res = a * b
        print(res)
        return res
    except TypeError:
        print("Введены не верные данные")
         