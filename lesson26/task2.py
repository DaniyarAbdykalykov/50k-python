def foo(**kwargs):
    for k, v in kwargs.items():
        print(f'"{k}": "{v}"')
        print('{"', k, '": "', v, '"}', sep="")

foo(color="green", font="Arial")