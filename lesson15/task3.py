numb = int(input("Введите число: "))
count = 0
my_set = []

while count < numb:
    inp_string = sorted(set(input("Введите строку: ")))
    my_set.append(inp_string)
    count += 1
print(my_set)