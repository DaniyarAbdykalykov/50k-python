age = int(input('Введите год вашего рождения: '))
category = input('Какую категорию вы хотите получить?(Введите латиницей): ')
category = category.upper()



if category == 'A':
    if age <= 2006:
        print("Да, вы можете получить водительские права категории 'A'")
    elif age - 2006 == 1:
        print(f'Вы можете получить права категории "A" через {age - 2006} год')
    elif age - 2006 < 5:
        print(f'Вы можете получить права категории "A" через {age - 2006} года')
    else:
        print(f'Вы можете получить права категории "A" через {age - 2006} лет')

if category == 'B':
    if age <= 2005:
        print("Да, вы можете получить водительские права категории 'B'")
    elif age - 2005 == 1:
        print(f'Вы можете получить права категории "B" через {age - 2005} год')
    elif age - 2005 < 5:
        print(f'Вы можете получить права категории "B" через {age - 2005} года')
    else:
        print(f'Вы можете получить права категории "B" через {age - 2005} лет')

if category == 'C':
    if age <= 2004:
        print("Да, вы можете получить водительские права категории 'C'")
    elif age - 2004 == 1:
        print(f'Вы можете получить права категории "C" через {age - 2004} год')
    elif age - 2004 < 5:
        print(f'Вы можете получить права категории "C" через {age - 2004} года')
    else:
        print(f'Вы можете получить права категории "C" через {age - 2004} лет')

if category == 'D':
    if age <= 2001:
        print("Да, вы можете получить водительские права категории 'D'")
    elif age - 2001 == 1:
        print(f'Вы можете получить права категории "D" через {age - 2001} год')
    elif age - 2001 < 5:
        print(f'Вы можете получить права категории "D" через {age - 2001} года')
    else:
        print(f'Вы можете получить права категории "D" через {age - 2001} лет')


