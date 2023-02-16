resume = {
    "name": "Jon",
    "age": 35,
    "skills": ["борьба", "стрельба", "вождение", "бокс"],
    "favourite_things": {"спорт": "ММА", "цвет": "черный", "мультфильм": "аватар", "еда": "стейк", "машина": "Cadillac"},
    "целеустремленный": True
}

age_in_2030 = 2030 - 2023 + resume["age"]
print(age_in_2030)

resume["age"] = age_in_2030

resume["name"] = resume["name"].upper()

# print(resume)

if resume["целеустремленный"]:
    print("Отлично! Я верю в тебя!")
else:
    print("Просто ты еще не нашел свою мечту")

print(f'любимая еда - {resume["favourite_things"]["еда"]}, любимый мультфильм - {resume["favourite_things"]["мультфильм"]}')
print(resume["skills"][1::2])