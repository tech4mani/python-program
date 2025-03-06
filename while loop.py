#WHILE LOOP   
a=0
while a < 10:
    a+=1
    print(a)



a = 5
b = 0
while(a > 0):
    b=b+ a
    a=a-1
print(b)

#FACTORIAL
n=int(input("enter a number:"))
a=1
while n >=1:
    a=a*n
    n=n-1
    print(a)

# #PRIME NUMBER
n=int(input("enter a number:"))
i=2
isprime=True
while i<=n//2:
    if n%i==0:
        isprime = False
        break
    i+=1
if isprime and n>1:
    print(f"{n} is a prime number")
else:
    print(f"{n} iS not a prime number")    
    
 
    