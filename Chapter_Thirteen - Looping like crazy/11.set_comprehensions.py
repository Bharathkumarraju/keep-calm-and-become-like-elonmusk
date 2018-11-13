# How to determine the  difference between dict comprehensions and set comprehensions
print("\n"*2)
# A literal set is surrounded by the curly braces, as are literal dictionaries
# In order to tell them apart look for the colon character used as delimiter in dictionaries, as the colon has no meaning in sets
# Quickly determine Whether a curly braced comprehension is dictcomp or a setcomp: look for the colon

# If the colon is there inside the curly braces then it is a dictcomp , If not it's a setcomp

vowels = { 'a', 'e', 'i', 'a', 'i', 'e', 'o', 'a', 'u', 'o' }
message = "Don't forget to pack your towel."

found = set()

for i in vowels:
    if i in message:
        found.add(i)

print(found)


print("\n"*2)


# How to use Set Comprehension here
found2 = { i for i in vowels  if i in message }
print(found2)

print("\n"*2)

# When a code is surrounded by [ and ] then you are looking at list comprehension

# when a code is surrounded by { and } then you are looking at either a set or a dictionary comprehension

# A dictcomp is easy to spot thanks to its use of the colon character as a delimiter

# tuple comprehensions don't exists at all

# [ .. code .. ] --> I am a list comprehension

# { .. code .. } --> I am a dict comprehension

# ( .. code .. ) --> I am a special case

# Tuples are immutable, Once a tuple is created it can not be changed.

# Python's four built-in data structures(tuples, lists, sets, and dictionaries) can be put to many uses.

#
