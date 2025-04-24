'''Lambda'''
square = lambda x:x**2
print(square(4))

'''Map'''
nums = [1,2,3]
square = list(map(lambda x:x**2,nums))
print(square)

'''Filter'''
nums = [1,2,3,4,5]
evens = list(filter(lambda x:x%2 == 0,nums))
print(evens)

'''Reduce'''
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x,y:x+y,nums)
print(product)