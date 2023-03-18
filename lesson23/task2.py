num = input("Введите числа через пробел: ")
num_lst = num.split()

num_lst_2 = list(map(lambda x: int(x) * 10, num_lst))

print(num_lst_2)