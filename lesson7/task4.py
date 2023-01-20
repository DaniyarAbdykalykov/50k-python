scholarship = 50

GPA = float(input('Введите Ваш средний балл за все предметы: '))

additional_sections = int(input('В скольких кружках Вы состоите? '))

volunteer = input('Если Вы занимались волонтерской деятельностью, напишите "да": ')
volunteer = volunteer.lower()

if GPA > 3.5:
    scholarship += 100

if additional_sections in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    scholarship += additional_sections * 30

if volunteer == 'да':
    scholarship += 50

print(f'Ваша стипендия составляет {scholarship}$')