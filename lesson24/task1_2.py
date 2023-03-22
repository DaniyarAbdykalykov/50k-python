stdin = input().split()

def unpack(*args):
    for i in args:
        print(float(i))

unpack(*stdin)