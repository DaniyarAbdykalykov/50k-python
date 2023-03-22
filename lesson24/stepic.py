def D(f):
    def derivative(x):
        return (f(x + 0.00001) - f(x)) / 0.00001
    return derivative

def f(x):
    return x ** 2

g = D(f)

print(g(5))