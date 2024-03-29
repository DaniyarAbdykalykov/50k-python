class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    def print_protected_data(self):
        print(self.__name, self.__balance, self.__passport)

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 4579527)
account1._BankAccount__print_private_data()
# print(dir(account1))
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)