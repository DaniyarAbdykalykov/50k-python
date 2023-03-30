class Computer:
    hdd = 1000
    ram = 16
    model = "HP 350 G2"
    power = 100
    is_working = False
    
    def turn_on(self):
        self.is_working = True
        self.power -= 1


comp = Computer()
print(comp.is_working)
print(comp.power)

comp.turn_on()
print(comp.is_working)
print(comp.power)
