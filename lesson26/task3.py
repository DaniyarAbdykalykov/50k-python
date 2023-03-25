def foo(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        new_dict[v] = k
    return new_dict


print(foo(color="green", font="Arial"))