number = int(input('Введите число: '))

if number % 5 == 0:
    print('Да')
else:
    print('Нет')

print('Да') if number % 5 == 0 else print('Нет')