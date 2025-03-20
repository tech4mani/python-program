# 1
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# n=0
# def num(a,b):
#     if n<a:
#         print(a,"is positive number")
#     if n>b:
#         print(b,"is negative number")
#     else:
#         print("0")
# num(a,b)

# 2
# sum=int(input("enter a number:"))
# i=int(input("enter a number:"))
# def cal(sum,i):
#         a=sum+i
#         b=sum-i
#         c=sum*i
#         d=sum%i
#         print(a)
#         print(b)
#         print(c)
#         print(d)
# cal(sum,i)
# 3
# n=int(input("enter a number:"))
# a=lambda b:b+20
# print(a(n))

# 2
# sum=int(input("enter a number:"))
# i=int(input("enter a number:"))
# def cal(sum,i):
#         print(sum+i)
#         print(sum-i)
#         print(sum*i)
#         print(sum%i)
# cal(sum,i)
# 4
# lambda function
# a=lambda x,y:x*y
# print(a(5,10))

#5
# n=10
# a=0
# b=1
# print(f"{a} {b}",end=" ")
# for i in range(n-2):
#     c=a+b
#     print(c,end=" ")
#     a=b 
#     b=c
#5#2
# def fun(n):
#     a=0
#     b=1
#     print(f"{a} {b}",end=" ")
#     for i in range(n):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# fun(10)

# 6.square root 
# n=float(input("enter a number:"))
# sq=n ** 0.5
# print(f"the square root is:{sq}")

# #7
# def greet(name):
#     print("hollo",name)
# greet("mani!")

# 8
# def sum_of_two():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     return a+b
# sum=sum_of_two()
# print(sum)

# 9
# def welcome_msg(name,msg="welcome!"):
#     print(f"{name} {msg}")
# welcome_msg("mani")
# welcome_msg("mani"" how are you")

# #10
# def info(name="mani",age=21,city="pudukkottai"):
#     print(f"my name is {name} i am {age} yaer old and i live in {city}")
# info()

# #10#2
# def info(name,age,city):
#     print(f"my name is {name} i am {age} yaer old and i live in {city}")
# info("mani",21,"pudukkottai")

#11
# def av(*num):
#     if len(num)==0:
#         return 0
#     return sum(num)/len(num)
# print(av(10,20,30,40))

#12
# def sum_of_two():
#     a=list(map(int,input("enter a number:").split()))
#     b=2
#     return list(n*b for n in a)
# sum=sum_of_two()
# print(sum)

#13
# def fc(n):
#     if n==0:
#         return 1
#     else:
#         return n*fc(n-1)
# n=int(input("enter a number:"))
# print(fc(n))

# #14
# def swap(a,b):
#     a,b=b,a
#     return a,b
# a=5
# b=6
# print(swap(a,b))

#15
# def lm(x):
#     z=lambda y:y*5
#     return z(x)
# print(lm(6))
#15#2
# z=lambda x,y:x*y
# a=z(5,6)
# print(a)
#16


#17
# def pal():
#     x="rotor"
#     rev=x[::-1]
#     if x==rev:
#         print(x)
#     else:
#         print("no palintrom")
# pal()

# #18
# n = 23
# x = 0
# for i in range(2,n):
#   if n%i==0:
#     x = 1
#     break
# if x == 1:
#   print(n,'Not Prime')
# else:
#   print(n,"Prime")

#19

#20
# String = input('Enter the string :')
# count = 0
# for i in String:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count+=1
# if count == 0:
#     print('No vowels found')
# else:
#     print('Total vowels are :' + str(count))

#21
# def maximum(a,b,c):
#     print(max(a,b,c))
# maximum(5,6,7)