 #(oops)object orient programing system
class studyhall:
    def student(self):
        print("student study time is going on...")
    def lecture(self):
        print("in order to guide student lecture is now available in studyhall")
studentNila = studyhall()
lecturesona = studyhall()
studentNila.student()

##using variable and function in class
class studyhall:
    name="sona"
    def student(self):
        print("student study time is going on...")
    def lecture(self):
        print("in order to guide student lecture is now available in studyhall")
studentNila = studyhall()
lecturesona = studyhall()
studentNila.student()
studentNila.name = "nila"
print(studentNila.name)

# #Default constructor:
class laptop:
    def __init__(self):
        print("demo")
    def display (self):
        print("display")
hp=laptop()


# #parameterized constructor:
class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
e1 = employee("bhavana",24)
e2 = employee("bharat",24)
print("name:{}".format(e1.name))  #using this one method
print("age:{}".format(e1.age))
print("name:{}".format(e2.name))
print("age:{}".format(e2.age))
print(f"age:{e1.age}")    #using this method for format print
print(f"name:{e1.name}")
print(f"age:{e2.age}")
print(f"name:{e2.name}")

#1        
class person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
b1 = person("mani",21,"pudukkottai")
print(f"Name   :{b1.name}")
print(f"Age    :{b1.age}")
print(f"Address:{b1.address}")
# 2
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposite(self,amount):
        self.balance += amount
        print(f"deposited: {amount}.balance:{self.balance}")
    def withdraw(self,Withdraw_amount):
        if Withdraw_amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= Withdraw_amount
            print(f"withdraw amount: {Withdraw_amount},New balance: {self.balance}")
# x=int(input("account balance:"))
y=int(input("deposite amount:"))
z=int(input("with_draw amount:"))
acount = BankAccount("mani",1000)
print(f"Account Holder:{acount.account_holder}")
print(f"Initial Balance:{acount.get_balance()}")

acount.deposite(y)
acount.withdraw(z)


#2#2method
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"deposited: {amount}.balance:{self.balance}")
    def withdraw(self,Withdraw_amount):
        if Withdraw_amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= Withdraw_amount
            print(f"withdraw amount: {Withdraw_amount},New balance: {self.balance}")
y=int(input("deposite amount:"))
z=int(input("with_draw amount:"))
acount = BankAccount("mani",1000)
print(f"Account Holder:{acount.account_holder}")
print(f"Initial Balance:{acount.balance}")
acount.deposite(y)
acount.withdraw(z)

#3
##area = (lenth)X(width)
##perimeter=2((l)x(w))
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"area of the rectangle:{area}")
    def perimeter(self):
        perimeter = 2*(self.length+self.width)
        print(f"perimeter of rectangle:{perimeter}")
len = int(input("length of rectangle:"))
wid = int(input("width of rectangle:"))
angle = Rectangle(len,wid)
angle.area()
angle.perimeter()

#4#Book
class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def info(self):
        return (f"TITLE:{self.title} , AUTHOR:{self.author} , PRICE:{self.price}")
book1 = book("well_said","mani",5000)
print(book1.info())

#5(student class)
class student:
    def __init__(self,name,roll_no,mark):
        self.name = name
        self.roll = roll_no
        self.mark = mark
    def total_mark(self):
        return sum(self.mark.values())
    def average_mark(self):
        return sum(self.mark.values())/len(self.mark)
student1 = student("mani","s121",{"math":60,"english":80,"science":75})
print("Total Mark:",student1.total_mark())
print("Average Mark:",student1.average_mark())

#6(car)
class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def car_info(self):
        return (f"{self.year} {self.make} {self.model}")
car1 = car("toyota","corolla",2020)
print(car1.car_info())

#7
import time
class Timer:
    def __init__(self):
        self.start_time = None
    def start(self):
        self.start_time = time.time()
    def elapsed_time(self):
        if self.start_time is None:
            return "Timer not started"
        return time.time() - self.start_time
timer = Timer()
timer.start()
time.sleep(2)
print("Elapsed Time:",timer.elapsed_time())

#8shopping car
class shoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,name,price):
        self.items.append({"name":name,"price":price})
    def total_price(self):
        return sum(item["price"] for item in self.items)
cart = shoppingCart()
cart.add_item("Apple",10)
cart.add_item("banana",25)
cart.add_item("Dragon",35)
print("Total price:",cart.total_price())

#9
##bank deposite and withdraw
class person:
    def __init__(self,balance):
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"deposited {amount}.balance{self.balance}")
    def withdraw(self,Withdraw_amount):
        if Withdraw_amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= Withdraw_amount
            print(f"withdraw amount {Withdraw_amount},balance of with_draw {self.balance}")
x=int(input("account balance:"))
y=int(input("deposite amount:"))
z=int(input("with_draw amount:"))
acount = person(x)
acount.deposite(y)
acount.withdraw(z)

#10
##fomula
#temprature:celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
#if (celsius * 9/5) + 32:
#K = °C + 273.15

class temprature:
    def __init__(self,celsius):
        self.celsius = celsius
    def fahren_heit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print(f"fahrenheit:{fahrenheit}.celsius:{self.celsius}")
    def kelvin(self):
        Kelvin = self.celsius + 273.15
        print(f"kelvin:{Kelvin}")
x = float(input("Enter temperature in Celsius: "))
celsius = temprature(x)
celsius.fahren_heit()
celsius.kelvin()