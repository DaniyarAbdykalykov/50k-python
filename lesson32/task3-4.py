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

    

    def set_bow_type(self, bow_type):
        bows = ("wooden", "aluminum", "carbon")
        if bow_type in bows:
            self.__bow_type = bow_type
        else:
            print("Такого вида лука не существует") 
        
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


class Sniper(Elves):
    speciality = "sniper"
    __arrowheads_ordinary = 0
    __arrowheads_round_with_paint = 0
    __arrowheads_silver_against_monster = 0
    __arrowheads_thin_with_poison = 0
    __arrowheads_heavy = 0

    def __init__(self, name, tribe, number_of_arrow, lord, age=1, hair_color="Black", bow_type="aluminum", type_arrowheads="ordinary"):
        super().__init__(name, tribe, number_of_arrow, lord, age, hair_color, bow_type)
        if type_arrowheads == "round with paint":
            self.__arrowheads_round_with_paint = number_of_arrow
        elif type_arrowheads == "silver against monsters":
            self.__arrowheads_silver_against_monster = number_of_arrow
        elif type_arrowheads == "thin with poison":
            self.__arrowheads_heavy = number_of_arrow
        elif type_arrowheads == "ordinary":
            self.__arrowheads_ordinary = number_of_arrow
        else:
            print('Таких стрел не существует')

    def improve(self):
        if self.rank == 5:
            print('Я достиг максимального ранга!')
        else:
            self.rank += 1
            print(f'Я улучшил свои навыки и получил {self.rank}-й ранг!')
            if self.rank == 5:
                self.__bow_type = "carbon"
                print(f'Ура! Теперь у меня {self.__bow_type} лук')

    def set_arrowheads(self, type_arrowheads):
        arrowheads = ('round with paint', 'silver against monsters', 'thin with poison', 'heavy')
        if type_arrowheads in arrowheads:
            self.__type_arrowheads = type_arrowheads
        else:
            print('Таких стрел не существует')
    def get_arrowhead(self):
        return self.__type_arrowheads    




elf_1 = Elves("Legolas", "Sindar", 20, "Tranduill", 455, "Golden")
elf_1.set_bow_type("still")
print(elf_1.get_attr())
