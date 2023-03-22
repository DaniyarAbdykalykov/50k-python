def inside():
    print("123")
    print(2464)

def outside(f):
    f()

outside(print)
outside(inside)