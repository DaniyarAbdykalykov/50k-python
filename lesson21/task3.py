def mymax(lst: list):
    for i in range(len(lst)):
        m = i
        for j in range(len(lst)):
            if lst[j] > lst[m]:
                m = j
        return lst[m]

my_lst = [2, 4, 30, 1, 5]

a = mymax(my_lst)
print(a)