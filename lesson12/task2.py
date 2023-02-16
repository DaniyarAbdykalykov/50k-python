lst_numbers = list(map(int, input().split()))

lst_numbers.remove(min(lst_numbers))
lst_numbers.remove(max(lst_numbers))

print(sum(lst_numbers) / len(lst_numbers))