num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

if num_1 < num_2:
    i = num_1
    while i < num_2 + 1:
        if i % 3 == 0:
            print(i)
        i += 1
elif num_1 > num_2:
    i = num_1
    while i > num_2 - 1:
        if i % 3 == 0:
            print(i)
        i -= 1