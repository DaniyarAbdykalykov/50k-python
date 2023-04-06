class Car:
    maker = ""
    model = ""
    weight = 2000

    def __init__(self, **kwargs):
        self.maker = kwargs["maker"]
        self.model = kwargs["model"]

    def add(self, kg):
        self.weight += kg

    def __str__(self):
        return self.maker


class MersedesBenz(Car):
    maker = "Mers"

    def __init__(self, **kwargs):
        model = kwargs["model"]
        super().__init__(model=model, maker=self.maker)

lada = Car(model="Kalina", maker="Lada")
print(lada.weight)
lada.add(30)
print(lada.weight)
print(lada)

e350 = MersedesBenz(model="E350", maker="Mers")

print(e350)

print(e350.model)
print(e350.maker)