# Getter & Setter

# public and private

class Employee:
    def __init__(self, name, age, nid):
        self.name = name # PUBLIC
        self._age = age # PROTECTED
        self.__nid = nid # PRIVATE

    def get_nid(self):  # getter
        return self.__nid
    
    def set_nid(self, nid):
        self.__nid = nid
        return nid

e1 = Employee("Choyon", 23, 123456789) # object

print("E1 INFO")
print(e1.name)
print(e1._age)

new_nid = e1.set_nid("345567785")
print(new_nid)

# e2 = Employee(
#     name = "Farhan",
#     age = 23,
#     nid = 12223456789
# )

# print("E2 INFO")
# print(e2.name)

from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod # abstract method
    def deposit(self, amount):
        print("deposit")

    def withdraw(self):
        print("withdraw")

class SaveingAccount(BankAccount):
    def save(self, amount):
        print("save")

    def withdraw(self):
        print("withdraw")

b1 = SaveingAccount()
b1.save(500)
    