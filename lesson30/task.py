class Elves:
    number_of_eyes = 2
    number_of_hands = 2
    number_of_legs = 2
    hair_color = 'black'
    rank = 1
    speciality = 'archer'

    def __init__(self, name, tribe, number_of_arrow, lord, bow_type="Wooden",):
        self.name = name
        self.tribe = tribe
        self.__number_of_arrow = number_of_arrow
        self.__lord = lord
        self.__bow_type = bow_type

    def greeting(self):
        print(f'''Мой господин {self.__lord}! Вас приветсвует {self.name}, воин-{self.speciality} {self.rank}-го ранга из племени {self.tribe}!''')

    def improve(self):
        if self.rank == 5:
            print('Я достиг максимального ранга!')
        else:
            self.rank += 1
            print(f'Я улучшил свои навыки и получил {self.rank}-й ранг!')
            if self.rank == 5:
                self.speciality = "sniper"
                print(f'Ура! Теперь я {self.speciality}')



class Wizards:
    number_of_eyes = 2
    number_of_hands = 2
    number_of_legs = 2
    hair_color = 'white'
    rank = 1
    speciality = 'magician'

    def __init__(self, name, squad, element, weapon, amount_of_mana, lord):
        self.name = name
        self.squad = squad
        self.element = element
        self.__weapon = weapon
        self.amount_of_mana = amount_of_mana
        self.__lord = lord

    def greeting(self):
        print(f'''Мой господин {self.__lord}! Вас приветсвует {self.name}, волшебник-{self.speciality} {self.rank}-го ранга из отряда {self.squad}!''')

    def improve(self):
        if self.rank == 5:
            print('Я достиг максимального ранга!')
        else:
            self.rank += 1
            print(f'Я улучшил свои навыки и получил {self.rank}-й ранг!')
            if self.rank == 5:
                self.speciality = "archmage"
                print(f'Ура! Теперь я {self.speciality}')

    def mana_reduction(self, mana: int | float):
        self.amount_of_mana -= mana

    def mana_increase(self, mana: int | float):
        self.amount_of_mana += mana
        

elf_1 = Elves("Legolas", "Sindar", 90, "Thranduil")
wizard_1 = Wizards('Gandalf', 'Maiar', 'air', 'staff', 100, 'Manwe')


elf_1._Elves__lord = "Sauron"

print(elf_1._Elves__lord)