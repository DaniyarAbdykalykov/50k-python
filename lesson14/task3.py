numbs_sep_by_spaces = set(map(int, input("Введите несколько чилел через пробел: ").split()))

numbs_seb_by_commas = set(map(int, input("Введите несколько чисел через запятую: ").split(",")))

unoin_of_numbs = numbs_sep_by_spaces & numbs_seb_by_commas
unoin_of_numbs = list(unoin_of_numbs)
unoin_of_numbs.sort(reverse=True)

print(unoin_of_numbs)