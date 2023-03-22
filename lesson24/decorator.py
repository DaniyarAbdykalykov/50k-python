def mydecorator(my_f):
    def wrap():
        print("Начало от декоратора")
        print(f"Сейчас вызовется функция {my_f}")
        my_f()
        print("Декоратор закончил сове исполнение")
    return wrap


@mydecorator
def myfunction():
    print("Основная функция запушена")
    print("Основная функция запушена")
    print("Основная функция запушена")


# mydecorator(myfunction)()
myfunction()