numbs_lst = list(map(int, input("Введите числа: ").split()))

numbs_dict = {}

for index, element in enumerate(numbs_lst):
    numbs_dict[index] = element ** 2

for key, value in numbs_dict.items():
    print(key, value)