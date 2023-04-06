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
    
    def set_attr(self, number_of_arrow, lord, bow_type):
        self.__number_of_arrow = number_of_arrow
        self.__lord = lord
        self.__bow_type = bow_type

    def get_attr(self):
        return f'Тип моего лука - {self.__bow_type}, стрел к нему {self.__number_of_arrow}. Мой господин {self.__lord}'

    def __str__(self):
        return f'Я {self.name} из племени {self.tribe}'
        

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

    def set_attr(self, weapon, lord):
        self.__weapon = weapon
        self.__lord = lord

    def get_attr(self):
        return f'Мое оружие - {self.__weapon}, мой господин - {self.__lord}'

    def __str__(self):
        return f'Я {self.name} из отряда {self.squad}'
        

elf_1 = Elves("Legolas", "Sindar", 90, "Thranduil")
wizard_1 = Wizards('Gandalf', 'Maiar', 'air', 'staff', 100, 'Manwe')

