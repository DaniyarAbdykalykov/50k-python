numbs_lst = list(map(int, input("Введите числа через запятую: ").split(",")))

l = len(numbs_lst)
for i in range(l):
    if i < l / 2 - 1.6:
        print(numbs_lst[i] * 2, end=" ")
    elif i > l / 2 - 1.6 and i < l / 2 - 0.6:
        print(numbs_lst[i] * 2)
    elif i > l / 2 - 1.6 and i < l - 1:
        print(numbs_lst[i] ** 2, end="-")
    elif i == l - 1:
        print(numbs_lst[i] ** 2)