from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def speak(self):
        print(f"{self._name} speaks")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def speak(self):
        print(f"{self._name} speaks")

    def purr(self):
        print(f"{self._name} purrs")





class Dog(Animal):
    def speak(self):
        print(f"{self.get_name()} speaks")


class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("the area is 1434")

class Rectangle(Shape):
    def area(self):
        print("the area of this rectangle is 12351305")


rectangle = Rectangle()
circle = Circle()

circle.area()

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def view_balance(self):
        print(self._balance)

bankacccount = BankAccount(123, 0)

class Payment(ABC):
    @abstractmethod
    def authorize_transaction(self):
        pass

class PaypalPayment(Payment):
    def authorize_transaction(self):
        print("paid with paypal")


class CreditCardPayment(Payment):
    def authorize_transaction(self):
        print("paid with credit card")

class DebitCardPayment:
    def authorize_transaction(self):
        print("paid with debit card")

creditcard = CreditCardPayment()
paypal = PaypalPayment()
debitcard = DebitCardPayment()


debitcard.authorize_transaction()


#implementing the authroize transaction method as an abstract method ensures all payments must authorize, allows it to be flexible
# to add more payment methods
#ensures all childs of payment must include an authroize transaction