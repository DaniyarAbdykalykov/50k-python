lst = [1, 0, [0], '-1', -33, 1.0, [1], '0', True, '1', False, 0.0]

num_1 = lst.count(1) + lst.count('1') + lst.count([1])
num_0 = lst.count(0) + lst.count('0') + lst.count([0])

print(f'Значений равных единице {num_1}\n\
Значений равных нулю {num_0}')

del lst[5:]
del lst[:3]