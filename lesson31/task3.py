class Humanoid_character:
    number_of_eyes = 2
    number_of_hands = 2
    number_of_legs = 2
    rank = 1

    def __init__(self, name, age=1, hair_color="black"):
        self.name = name
        self.age = age
        self.hair_color = hair_color


class Elves(Humanoid_character):
    speciality = 'archer'

    def __init__(self, name, tribe, number_of_arrow, lord, age=1, hair_color="Black", bow_type="Wooden"):
        super().__init__(name, age, hair_color)
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
    
    def shooting(self):
        if self.__number_of_arrow > 0:
            self.__number_of_arrow -= 1
        else:
            print("У меня закончились стрелы")

    def replenishment(self, replenishment_amount: int):
        if replenishment_amount > 0:
            if self.__number_of_arrow + replenishment_amount > 30:
                self.__number_of_arrow = 30
                print("Колчан для стрел полон")
            else:
                self.__number_of_arrow += replenishment_amount
        else:
            print("Введите правильные данные")

    def set_attr(self, number_of_arrow, lord, bow_type):
        self.__number_of_arrow = number_of_arrow
        self.__lord = lord
        self.__bow_type = bow_type

    def get_attr(self):
        return f'Тип моего лука - {self.__bow_type}, стрел к нему {self.__number_of_arrow}. Мой господин {self.__lord}'



    def set_lord(self, lord):
        self.__lord = lord

    def get_lord(self):
        return self.__lord

    def del_lord(self):
        del self.__lord

    lord = property(get_lord, set_lord, del_lord)


    def __str__(self):
        return f'Я {self.name} из племени {self.tribe}'




class Wizards(Humanoid_character):
    speciality = 'magician'

    def __init__(self, name, squad, element, weapon, amount_of_mana, lord, age=1, hair_color="White"):
        super().__init__(name, age, hair_color)
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

    def set_lord(self, lord):
        self.__lord = lord

    def get_lord(self):
        return self.__lord

    def del_lord(self):
        del self.__lord

    lord = property(get_lord, set_lord, del_lord)

    def __str__(self):
        return f'Я {self.name} из отряда {self.squad}'

