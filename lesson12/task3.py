musical_instruments = ['гитара', 'фортепиано', 'комуз', 'саксофон', 'виолончель', 'барабан', 'арфа', 'флейта']


print(f"все струнные инструменты: {musical_instruments[::2]}")
print(f"все не струнные инструменты: {musical_instruments[1::2]}")
print(f"перевернутый список: {musical_instruments[::-1]}")
print(musical_instruments[3:5:])
print(musical_instruments[::-3])