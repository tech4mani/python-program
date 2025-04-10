##Abstraction
#1
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(Animal):
    def make_sound(self):
        return "woof!"
class cat(Animal):
    def make_sound(self):
        return "Meow!"
dog = dog()
cat = cat()
print(dog.make_sound())
print(cat.make_sound())

#2
from abc import ABC,abstractmethod
class vechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class car(vechile):
    def start_engine(self):
        return "car engine started"
    def stop_engine(self):
        return "car engine stopped"
class Bike(vechile):
    def start_engine(self):
        return "bike endine started"
    def stop_engine(self):
        return "bike engine stopped"
car1 = car()
bike = Bike()
print(car1.start_engine())
print(bike.stop_engine())

#3
# Create an abstract class Shape with:
# An abstract method area()
# An abstract method perimeter()
# Then create two classes Rectangle and Circle that implement these methods.

from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(shape):
    def area(self):
        print("area of rectangle")
    def perimeter(self):
        print("perimeter of rectangle")
class Circle((shape)):
    def area(self):
        print("area of circle")
    def perimeter(self):
        print("perimeter of circle")
rect = Rectangle()
circ = Circle()
rect.area()
rect.perimeter()
circ.area()
circ.perimeter()

#4
# Create an abstract class Payment with:
# An abstract method make_payment(amount)
# Then, create subclasses:
# CreditCardPayment
# PayPalPayment
# Each class should implement make_payment() differently.

from abc import ABC , abstractmethod
class payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
class CreditCard(payment):
    def make_payment(self,amount):
        self.amount = amount
        print(f"paid ${amount} using creditcard")
class PayPal(payment):
    def make_payment(self,amount):
        self.amount = amount
        print(f"transaction ${amount} using PayPal")
credit = CreditCard()
pay = PayPal()
credit.make_payment(1000)
pay.make_payment(20000)

#5
# Create an abstract class Animal with:
# An abstract method speak()
# An abstract method move()
# Then create:
# Bird class (speak: "chirp", move: "flies")
# Fish class (speak: "blub", move: "swims")

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def method_speak(self):
        pass
    @abstractmethod
    def method_move(self):
        pass
class Bird(Animal):
    def method_speak(self):
        return "chirp"
    def method_move(self):
        return "flies"
class Fish(Animal):
    def method_move(self):
        return "blub"
    def method_speak(self):
        return "swims"
bird = Bird()
fish = Fish()
for animal in (bird,fish):
    print(f"The animal moves by: {animal.method_move()}")
    print(f"The animal speaks like: {animal.method_speak()}")
