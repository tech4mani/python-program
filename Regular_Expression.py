'''regular expression'''
'''Re.Match()'''
import re 
x = "a"
if re.match('.',x):
    print("yes")
else:
    print("No")

'''more the one character'''
import re 
x = "apple"
if re.match('^',x):
    print("yes")
else:
    print("No")

'''Re.search()'''
import re
result = re.search(r"world","hello world")# the word only small or capital letter
print(result.group())

'''Re.findall()'''
import re
result = re.findall(r"\d+","My number is 123,and my friend's number is 456.")
print(result)

'''Re.finditer()'''
import re 
matches = re.finditer(r"\d+","My number is 123,and my friend's number is 456.")
for match in matches:
    print(match.group())

'''Re.sub()'''
import re 
result=re.sub(r"\d+","###","My number is 123 and 456.")
print(result)

'''Re.split()'''
import re 
result = re.split(r"\s+","Mani Rohan Sadhosh")
print(result)
 