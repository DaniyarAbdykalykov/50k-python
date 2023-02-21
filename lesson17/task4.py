numbs_lst = list(map(int, input("Введите числа через запятую: ").split(",")))

for i in range(len(numbs_lst)):
    if i < len(numbs_lst) / 2 - 2:
        print(numbs_lst[i] * 2, end=" ")
    elif i == len(numbs_lst) / 2 - 1:
        print(numbs_lst[i]) * 2
    elif i > len(numbs_lst) / 2 - 1:
        print(numbs_lst[i] ** 2, end="-")
    elif i == max(numbs_lst) - 1:
        print(numbs_lst[i])

