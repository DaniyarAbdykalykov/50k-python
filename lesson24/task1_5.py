def introduce(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

debug = __debug__


def introduce_on_debug(func):
    if not debug:
        return func
    
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    
    return wrapper


def optional_introduce(func):
    def wrapper(*args, introduce=False, **kwargs):
        if introduce is True:
            print(func.__name__)
            return func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper

# @introduce_on_debug
@optional_introduce
def identity(x):
    return x

print(identity(42, introduce=True))

def flip(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper

@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

# div(2, 4, show=True)


