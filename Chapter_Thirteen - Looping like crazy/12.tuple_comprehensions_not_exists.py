import os
print("\n"*2)
print("\t"*9, os.getcwd())
print("\n"*2)


# Tuple is immutable, Once tuple is created, it can not be changed
# This is also means that it's not possible to generate tuple's value in the code.

# Define a tuple
name = ()

# below code gives an ERROR

'''
for i in ( 'timo', 'robert', 'dat', 'paulo' ):
    name.append(i)
'''


print(type(name))
print("\n"*3)

for i in [x*3 for x in [1, 2, 3, 4, 5]]:
    print("\t"*i, i)

print("\n"*3)
# The above code as same as below one.

for i in (x*3 for x in [1, 2, 3, 4, 5, 6]):
    print("\t"*i, i)

# When you come across something that looks like a listcomp but is surrounded by parentheses, then it is called as a Generator.

print("\n"*3)