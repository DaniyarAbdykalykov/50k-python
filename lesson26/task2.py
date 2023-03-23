def foo(**kwargs):
    for k, v in kwargs.items():
        print(f'"{k}": "{v}"')

foo(color="green", font="Arial")