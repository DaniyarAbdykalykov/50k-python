lst = [
    ['цикл', 'переменная', 'функция', 'аргумент', 'условие'], 
    ['loop', 'variable', 'function', 'argument', 'condition']
]

my_dict = {}

for i in range(len(lst)):
    for j in range(len(lst[i])):
        my_dict[lst[1][j]] = lst[0][j]
print(my_dict)