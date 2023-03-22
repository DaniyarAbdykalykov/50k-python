def print_given(*args, **kwargs):
    for e in args:
        print(e, type(e))
    for e in kwargs:
        print(e, kwargs[e], type(kwargs[e]))


print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
