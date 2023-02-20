resume = {
    "name": "Jon",
    "age": 35,
    "skills": ["борьба", "стрельба", "вождение", "бокс"],
    "favourite_things": {"спорт": "ММА", "цвет": "черный", "мультфильм": "аватар", "еда": "стейк", "машина": "Cadillac"},
    "целеустремленный": True
}


for key, value in resume.items():
    print(f"***{value}***")