from random import choice

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = choice(lst)
        s_lst = []
        m_lst = []
        e_lst = []
        for n in lst:
            if n < q:
                s_lst.append(n)
            elif n > q:
                m_lst.append(n)
            else:
                e_lst.append(n)
        return quick_sort(s_lst) + e_lst + quick_sort(m_lst)


inp_lst = list(map(int, input("Введите числа через пробел: ").split()))

print(quick_sort(inp_lst))