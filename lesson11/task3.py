a = input('Введите первое слово: ')
b = input('Введите второе слово: ')

c = a.upper() + b.lower()
print(c)
print(c.replace('ч', "4"))
print(c.count('А') + c.count('а'))

if not c.endswith('.'):
    c = c + '.'

print(c)