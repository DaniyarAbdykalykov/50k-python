a = 50

b = 30

c = b - a       # -20 int

 

a = '50'

b = 30

c = a - b       # невозможно выполнить математическую операцию "минус" со строкой и целым числом

 

a = 1.0

b = 1.0

c = a - b       # 0.0 float

 

a = 25

b = 10.0

c = b - a       # -15.0 float

 

a = 5

b = 2.5

c = b * a       # 12.5 float

 

a = '3'

b = 3

c = a * b       # '333' str

 

a = '3 '

b = 3

c = b * a       # '3 3 3 ' str

 

a = '5'

b = 3.5

c = a * b       # невозможно умножить строку с вещественым числом