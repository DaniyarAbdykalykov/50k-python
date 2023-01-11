a = 10

b = -5.5

c = 2.0

d = -20

e = 0.5

f = 0

g = 3

 

res_1 = a + e - b * g           # 27.0 float

res_2 = a + (e - b) * g         # 28.0 float

res_3 = f * (a + b - e - d)     # 0.0 float

res_4 = g + c + e + b           # 0.0 float

res_5 = (90 + a + f) ** e       # 10.0 float