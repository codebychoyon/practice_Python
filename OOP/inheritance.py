# Inheritance

class BankAccount:
    def withdraw_money(self):
        print("Withdrawal successful")

b1 = BankAccount()

b1.withdraw_money()


class SavingAccount(BankAccount):
    pass

b2 = SavingAccount()
b2.withdraw_money()

class A:
    X=5

a1 = A()
a2 = A()
a1.x = 10
print(a2.X)