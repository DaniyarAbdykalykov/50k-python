numbs_tuple = ()

numb = int(input("Введите число: "))

while numb > 0:
    if numb not in numbs_tuple:
        numbs_tuple += (numb,)
    numb = int(input("Введите число: "))

print(sorted(numbs_tuple))