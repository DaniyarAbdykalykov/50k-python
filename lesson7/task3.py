num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if num_1 < num_2:
    print('Первое число меньше второго')

if num_1 * 2 == num_2:
    print('Первое число умноженное на два равляется второму числу')

if num_1 < 0:
    print("Первое число отрицательное")

if (num_2 - num_1)  % 2 == 0:
    print('Второе число минус первое число - четное')