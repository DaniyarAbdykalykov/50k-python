num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

if num_1 < num_2:
    for i in range(num_1, num_2 + 1, abs(num_3)):
        print(i, end="")
elif num_1 > num_2:
    for i in range(num_1, num_2 - 1, -abs(num_3)):
        print(i, end="")