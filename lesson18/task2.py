people = ['Regina', 'Erkayim', 'Begayim'] 
countries = ["Germany", 'France', 'Spain', 'Portugal', 'Holland', 'Japan', 'South Korea', 'Singapore']

for i in range(len(people)):
    for j in range(len(countries)):
        name = people[i]
        country = countries[j]
        print(f'{name} lives in {country}')