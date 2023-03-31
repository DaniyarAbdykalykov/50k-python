class Car:
    maker = ""

    def __init__(self, model, maker):
        self.model = model
        self.maker = maker


bmw = Car("X5", "BMW")

print(bmw.model)
print(bmw.maker)