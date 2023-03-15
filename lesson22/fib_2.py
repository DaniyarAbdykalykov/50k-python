fib = [1, 1]

n = 100

for i in range(n):
    new = fib[i] + fib[i+1]
    fib.append(new)


print(fib)