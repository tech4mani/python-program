'''File_handling'''
#1
# f = open("k.py")
# print(f)


#2#Read()
# f = open("k.py")
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

#3#character
# f = open("k.py")
# txt = f.read(60)
# print(type(txt))
# print(txt)
# f.close()

#4#Read line()
# f = open("k.py")
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

#5#read all line and return  o/p in list
# f = open('k.py')
# line = f.readlines()
# print(type(line))
# print(line)
# f.close()

#6#Another way to get all the lines as a list is using splitlines():
# f = open("k.py")
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

#7#opening file for writing and updating:
# with open("k.py",'a')  as f:
#     f.write("playtypus.lay_eggs()\n")
#     f.write("playtypus.lay_eggs2()\n")

#8
# with open("k.txt","w") as  f:
#     f.write("create and written")

#9#Deleting files:
# import os 
# if os.path.exists("k.txt"):
#     os.remove("k.txt")
# else:
#     print("The file does not exit")