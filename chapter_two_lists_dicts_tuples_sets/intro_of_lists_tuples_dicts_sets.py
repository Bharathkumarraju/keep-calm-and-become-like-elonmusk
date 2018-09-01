'''
Assigning a value to a variable

This value may be a Number or a String or an Object
'''

import random

print()
wait_time = random.randint(1,18)
print(wait_time)

word = "SRI ANJANEYAM"

for i in range(wait_time):
    print()
    print(word)
    print()
    print("Rama Lakshmana Janaki Jai Bholo Hanumaanuki")

# In python everything is an object
# Means that Numbers,Strings,Functions,Modules everything is an object.

# Python stores the collection of values


# Pythons Four Built-in Data Structures
# 1. list
# 2. tuple
# 3. dictionary
# 4. set

# 1. Lists are dynamic , They can grow and shrink on-demand
# 1. Lists are mutable, that means you can change a list at any time by adding,removing or changing objects



# 2. Tuple - An ordered list-like collection which is immutable that is it cannot change.
# 2. Tuple - once you assign objects to a tuple , the tuple cannot be changes under any circumstance
# 2. Tuple is a constant list
# 2. Tuples are like lists  except once created they CANNOT change, Tuple is an immutable list


'''
Lists and Tuples are great when you want to present data in an ordered way. such as list of destinations on a travel itinerary
where the order of destinations is important.

But sometime the order in which you present the data is not important,
for example: you might want to store some user details such as their id and password , but you don't care in which order they store
to store data like this, an alternative to python's list/tuple is needed,  here comes rescue as DICTIONARIES and SETS
'''

# 3. Dictionary - An unordered data structure - Dictionary, If keeping data in specific order isn't important you, but the structure is,
# 3. Dictionary and Set, Python comes with choice of two unordered data structures that are dictionary and set
# 3. dictionary -  An unordered set of key/value pairs, Like lists dictionaries can grow and shrink on-demand


# 4. Set - A data structure that avoids the duplicates
# 4. Set - an un-ordered set of unique objects, useful to remove the  duplicates quickly from any other collection
# 4. Set - is a collection of unordered unique items - no duplicates allowed









