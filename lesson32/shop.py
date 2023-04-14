class Good:
    is_sold = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sell(self, money_object):
        if self.is_sold:
            raise Exception('Товар уже продан')
        self.is_sold = True
        money_object.money += self.price
        return money_object


class Money:
    money = 0


class Computer(Good):
    hdd = 1000
    has_windows = True

    def __init__(self, price, model):
        name = f'Computer {model}'
        super().__init__(name=name, price=price)

class Laptop(Computer):
    def __init__(self, price, model):
        name = f"Laptop {model}"
        super(Computer, self).__init__(name=name, price=price)

class Printer(Good):
    def __init__(self):
        name = "Printer LaserJet 1080"
        price = 200
        super().__init__(name, price)


p_1 = Printer()
p_2 = Printer()

c_1 = Computer(1000, "Predator 2100")
c_2 = Computer(2000, "Predator 3100")
c_3 = Computer(3000, "Predator 4100")

l_1 = Laptop(price=1100, model="HP 350 G2")

m = Money()

print(m.money)
m = c_2.sell(m)
print(c_2.is_sold)
print(m.money)
m = p_1.sell(m)
print(p_1.is_sold)
print(m.money)
# m = c_2.sell(m)
