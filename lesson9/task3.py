num = int(input('Введите любое число: '))

if 99 < num < 1000:
    print(num % 10 % 3 == 0)
elif 9 < num < 100:
    print(num % 10 % 2 == 0)
else:
    print(num % 5 == 0)