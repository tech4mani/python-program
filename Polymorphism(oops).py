
##polymorphism:
#1
str1 = "python"
str2 = "programming"
print(str1 +" "+ str2)


#2
print(len("programing"))
print(len(["python","java","c"]))

#3
class cat:  
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"i am a cat my name is {self.name} i am {self.age} yaer old")
    def make_sound(self):
        print("Meow")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"i am dog my name is {self.name} i am {self.age} years old")
    def make_sound(self):
        print("Bark")
cat1 = cat("kitty",3)
dog1 = dog("fluffy",4)
for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

#4
class grocery:  
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def info(self):
        print(f"i bought a: {self.name} ")
        print(f"the amount of {self.name}:{self.price}")
    def make_shoping(self):
        print("shoping")
class milk:
    def __init__(self,protuct,price):
        self.protuct = protuct
        self.price = price
    def info(self):
        print(f"i bhought a: {self.protuct}")
        print(f"the amount of {self.protuct}: {self.price}")
    def make_shoping(self):
        print("shoping_mall")
grocery1 = grocery("rice","$250")
grocery2 = milk("Milk","$25")
for kadai in(grocery1,grocery2):
    kadai.make_shoping()
    kadai.info()

#5
class parent:
    def __init__(self,name):
        self.name = name
        print("parent class intialized")
    def speak(self):
        print("parent is speaking")
class child(parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
        print("child class initizalized")
    def speak(self):
        print("child is speaking")
parent = parent("slice")
child = child("Jhon",25)
parent.speak()
child.speak()