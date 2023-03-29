
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Произошла ошибка")
    print("Делить на ноль нельзя")
except ValueError:
    print("Ошибка")
    print("Возможно, ввод не верный")