# Сортировка выбором

num_lst = list(map(int, input("Введите числа через пробел: ").split()))

for i in range(len(num_lst) - 1):
    m = i
    j = i + 1
    while j < len(num_lst):
        if num_lst[j] < num_lst[m]:
            m = j
        j = j + 1
    num_lst[i], num_lst[m] = num_lst[m], num_lst[i]

print(num_lst)