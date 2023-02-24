inp_lst = list(map(int, input("Введите числа через пробел: ").split()))

lst_1 = []
count = 0
while count < len(inp_lst):
    lst_1.append(inp_lst[count] + 5)
    count += 1
print(lst_1)

lst_2 = []
for i in inp_lst:
    lst_2.append(i * 10)
print(lst_2)

lst_3 = [i ** 2 for i in inp_lst]
print(lst_3)