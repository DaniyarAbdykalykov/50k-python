a = 10

b = '10'

if a == b:         # не сработает, т.к. строку с числом нельзя сравнить

    print(f'Да, {a} == {b}')

 

a = '1000'

b = 'a'

if a < b:          # сработает, код символа "а" больше чем код символа "1". Сравнение строк идет по одному символу слева на право

    print(f'Да, {a} < {b}')

 

a = 'ABC'

b = 'abc'

if a > b:          # не сработает, код символа "а" больше символа "А", соответсвенно a < b

    print(f'Да, {a} > {b}')

 

a = 'abc'

b = 2

if a * b != 'abcabc':    # не сработает, 'abc' * 2 получится 'abcabc',

    print(f'Да, {a*b} != abcabc')

 

a = 'abc'

b = 'xyz'

if a + b == b + a:       # не сработает, 'abcxyz' не равен 'xyzabc'

    print(f'Да, {a+b} == {b+a}')

 

a = 25

b = 5

if a % b == 0:     # сработает, 25 делится без остатка на 5, соответсвенно 0 == 0

    print(f'Да, {a % b} == 0')

 

if True:     # сработает, для выполнения условия if необходимо  истина, чем является True

    print(f'True, это {True}')