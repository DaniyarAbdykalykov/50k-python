def myprint(n):
    print(n, end="\t")
    if n >5:
        print("> 5")
    else:
        print("<= 5")
    if n > 0:
        myprint(n-1)


myprint(10)