# #LARGEST THREE NUMBER
a=5
b=6
c=7
if a >b and a>c:
    print("a is largest")
elif b>c and b>a:
    print("b is largest")
else:
    print("c is largest")

# # ELIGIBLE TO VOTE OR NOT
mani="vote"
if (mani == "vote"):
    print("eligible to vote")
else:
    print("not eligible to vote")

#even or not
a=10
if a%2 == 0:
    print("even no")
else:
    print("not even no")  

#GRADE FOR A MARK
a=int(input("enter a no a:"))
b=int(input("enter a no b:"))
c=int(input("enter a no c:"))
d=int(input("enter a no d:"))
if 85 <= a <= 100:
    print("A Grade")
elif 60 <= b <= 84:
    print("B Grade")
elif 40 <= c <= 59:
    print("c Grade")
elif 35 <= d <= 39:
    print("d Grade")
else:
    print("fail")

#THE CHARACTER IS PRESENT OR NOT
a=input("enter a name:")
if "w" in a:
    print(" is present in hello world")
else:
    print(" is not present in hello world")

#FIND A LEAP YEAR OR NOT
a=int(input("enter a year:"))
b=a % 4==0
if b:
    print("is a leap year")
else: 
    print("is not a leap year")