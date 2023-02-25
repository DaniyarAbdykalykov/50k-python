num_1 = int(input("Введите число: "))
lst = []

count = 0
while count < num_1:
    num_lst = list(map(int, input("Введите числа через пробел: ").split()))
    amount_of_numbs = 0
    sum_of_numbs = 0
    for i in num_lst:
        sum_of_numbs += i
        amount_of_numbs += 1
    lst.append(sum_of_numbs / amount_of_numbs)
    count += 1

print(lst)