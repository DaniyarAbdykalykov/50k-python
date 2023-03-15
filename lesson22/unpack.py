def unpack(lst):
    for e in lst:
        if type(e) is list:
            unpack(e)
        else:
            print(e)



a = [4, 2, 5, [5, 2, 4], 25, [42, [53, 63, 8]]]
unpack(a)