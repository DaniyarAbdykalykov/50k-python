a = 50

b = -0.9

a += b            # 49.1 float

 

a = '123'

b = 3

a *= b            # '123123123' str 

 

a = 10

b = 0.5

a = (a * a) ** b  # 10 float

 

a = '5'

a = 5

b = a * a

a += b            # '555555' str

 

a = 5

a = '5'

b = a * a

a *= b            # переменная a после переопределения является строкой. Соотвественно, выражение b = a * a является ошибкой, т.к. строка на строку не умножается

 

a = 0.0

b = a * a + 25

a = b  / (a * b)  # b = 25.0, умножение на ноль дает ноль. Отсюда следует, что b не делится на 0.0