a = 144

b = 12

a //= b + b       # 6 int

 

a = 20

b = 5

a /= b + b        # 2.0 float

 

a = 2

b = a ** a ** 3

a *= b - b        # 0 int

 

a = 2

b = '5'

a *= b + b * a    # '555555' str

 

a = -3.5

b = (a + a) / 50

a /= b * b        # -178.571428 float