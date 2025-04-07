#inheritance
class parent:
    def first(self):
        print("this is a first function")
class child(parent):
    def second(self):
        print("this is a second function")
obj = child()
obj.first()
obj.second()

#Single inheritance:
class calculate:
    def sum(self,a,b):
        print(a+b)
class Number(calculate):
    pass
obj = Number()
obj.sum(8,9)

#Multiple Inheritance
class first:
    def __init__(self):
        self.greet = "hello"
class second:
    def __init__(self):
        self.name = "greeks"
class child(first,second):
    def __init__(self):
        first.__init__(self)
        second.__init__(self)
    def combine(self):
        print(self.greet,self.name)
        print("welcome to greet python.")
obj = child()
obj.combine()

#The Diamond problem:
class Hello:
    def func(self):
        print("hello")
class geek(Hello):
    def func(self):
        print("geeks")
class python(Hello):
    def func(self):
        print("geeks python")
class geekspython(geek,python):
    pass
obj = geekspython()
obj.func()

#Multi-level Inheritance:
class Grandpa:
    def __init__(self):
        self.age = 100
class parents(Grandpa):
    def __init__(self):
        self.name = "geek"
        Grandpa.__init__(self)
class Grandchild(parents):
    def __init__(self):
        self.hobby = "Gaming"
        parents.__init__(self)
    def display(self):
        print("Grandpa:",self.age)
        print("Grandchild:",self.name)
        print("Grandchild:",self.hobby)
obj = Grandchild()
obj.display()

#Hierarical inheritance
class calculate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def division(self):
        print(self.a / self.b)
class Add(calculate):
    def __init__(self, a, b):
        calculate.__init__(self,a,b)
    def add(self):
        print("addition:",self.a+self.b)
        Add.division(self)
class subtract(calculate):
    def __init__(self, a, b):
        calculate.__init__(self,a,b)
    def subtract(self):
        print("subtraction:",self.a - self.b)
        subtract.division(self)
obj1 = Add(10,20)
obj1.add()
obj2 = subtract(20,40)
obj2.subtract()

#Hybrid inheritance
class animal:
    def speak(self):
        print("Animal speak")
class mammal(animal):
    def give_birth(self):
        print("mammal gives birth")
class Bird(animal):
    def lay_eggs(self):
        print("bird lays_eggs")
class playtypus(mammal,Bird):
    pass
playtypus = playtypus()
playtypus.speak()
playtypus.give_birth()
playtypus.lay_eggs()
