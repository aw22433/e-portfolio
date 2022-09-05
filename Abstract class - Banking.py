from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def pay(self, ammount, payee):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

class Savings(Account):
    def __init__ (self, fixed_term_expired, balance):
        self.fixed_term_expired = fixed_term_expired
        self.balance = balance

    def pay(self, amount, balance):
        if self.fixed_term_expired == True:
            self.balance -= amount
            
        else:
            print('Unable to pay. Balance locked until fixed period expires')


    def withdraw(self, amount, balance):
        if self.fixed_term_expired == True:
            self.balance -= amount
            
        else:
            print('Unable to withdraw. Balance locked until fixed period expires')

    def deposit(self, amount, balance):
        self.balance += amount

saving = Savings(True, 100)
saving2 = Savings(False, 150)

saving.pay(50,saving.balance)
print(saving.balance)

saving.pay(20,saving.balance)
print(saving.balance)

saving2.pay(50,saving2.balance)
print(saving2.balance)

saving.withdraw(20,saving.balance)
print(saving.balance)

saving.deposit(50,saving.balance)
print(saving.balance)