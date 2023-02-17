numbs_sep_by_spaces = set(map(int, input("Введите несколько чилел через пробел: ").split()))
print(numbs_sep_by_spaces)

numbs_seb_by_commas = set(map(int, input("Введите несколько чисел через запятую: ").split(",")))
print(numbs_seb_by_commas)

unoin_of_numbs = numbs_sep_by_spaces & numbs_seb_by_commas
print(sorted(unoin_of_numbs))