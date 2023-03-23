def myprint(*args, mysep="---"):
    print(*args, sep=mysep)
    return len(args)

inpt = myprint(*input().split(', '))

print(inpt)