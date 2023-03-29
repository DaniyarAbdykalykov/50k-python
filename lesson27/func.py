def mydivision(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")

    return num_1 / num_2


a = int(input())
b = int(input())
print(mydivision(a, b))
print(3+2)