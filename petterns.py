#patterns
n=5
for i in range(1,n+1):
    print('* '*i)

# inverted triangle
n=5
for i in range (n,0,-1):
    print('* '*i)
    
# pryamid pattern
n=5
for i in range(1,n+1):
        print(" "*(n-i)+'*'*(2*i-1))

# inverted pryamid pattern
n=5
for i in range(n,0,-1):
        print(" "*(n-i)+'*'*(2*i-1))
        
#DIAMOND PATTERN
n=5
for i in range(-5,n+1):
    print(" "*(n-i)+'*'*(2*i-1))
    n=6
for i in range(n,0,-1):
        print(" "*(n-i)+'*'*(2*i-1))
#second method
n=5
for i in range(1,5):
    print(" "*(n-i)+'*'*(2*i-1))
for i in range(n,0,-1):
        print(" "*(n-i)+'*'*(2*i-1))


# #NUMBER PRAYMID
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for j in range(1*i):
        print(j+1,end=" ")
    print()

# inverted #NUMBER PRAYMID
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(1*i):
        print(j+1,end=" ")
    print()

#FLOYD'S TRIANGLE
for i in range(1,2):
    print(i)
for i in range(2,4):
    print(i,end=" ")
print()
for i in range(4,7):
    print(i,end=" ")
print()
for i in range(7,11):
    print(i,end=" ")
print()
for i in range(11,16):
    print(i,end=" ")
print()

#2
n=5
b=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(b,end=" ")
        b+=1
    print()
    

#hollow square pattern
for i in range(1,7):
    print("*",end=" ")
print()
for j in range(1,4):
    print("*","       ","*")
for i in range(6,0,-1):
    print("*",end=" ")

#hollow triangle  
n=4
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    
# * and _ pattern    
n=5
for i in range(1,n+1):
    for j in range(i):
        if j%2==0:
            print("*",end="")
        else:
            print("_",end="")
    print()