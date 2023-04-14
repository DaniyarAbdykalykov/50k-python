class Person:
    
    def can_breathe(sefl):
        print('я могу дышать')

    def can_walk(self):
        print('я могу ходить')

class Doctor(Person):

    def can_cure(self):
        print('я могу лечить')


class Architect(Person):

    def can_build(self):
        print("я могу посстроить здание")


d = Doctor()
a = Architect()

print(issubclass(Person, Doctor))
