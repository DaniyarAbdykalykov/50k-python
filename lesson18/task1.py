lst = [
    ['цикл', 'переменная', 'функция', 'аргумент', 'условие'], 
    ['loop', 'variable', 'function', 'argument', 'condition']
]

my_dict = {}

for i in range(len(lst)):
    for j in range(len(lst[i])):
        my_dict[lst[0][j]] = lst[1][j]
print(my_dict)