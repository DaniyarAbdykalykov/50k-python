class Computer:
    hdd = 1000
    ram = 16
    model = "HP 350 G2"
    power = 100
    is_working = False
    
    def turn_on(self):
        self.is_working = True
        self.power -= 1


hp_1 = Computer()
print(hp_1.ram)

hp_2 = Computer()
print(hp_2.ram)

hp_2.ram = 8
print(hp_2.ram)

print(type(hp_2))