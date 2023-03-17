revr_num = 0


def reverse(num):
    global revr_num
    if num > 0:
        last_digit = num % 10
        revr_num = revr_num * 10 + last_digit
        reverse(num // 10)
    return revr_num        


numbs = int(input())

print(reverse(numbs))