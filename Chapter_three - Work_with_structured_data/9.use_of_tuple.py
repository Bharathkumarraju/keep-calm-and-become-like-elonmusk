'''

tuple is like a list that can not be changed once it's created, tuples are immutable, they can not change.

having said that immutable data structures can often be useful

'''

# Tuples are surrounded by parentheses where as lists are surrounded by square brackets

print()
vowels = ['a', 'e', 'i', 'o', 'u']
print(type(vowels))
print(vowels)

print()
vowels = ('a', 'e', 'i', 'o', 'u')
print(type(vowels))
print(vowels)

print()
vowels = {'a': 1, 'e': 2, 'i': 1, 'o': 0, 'u': 10}
print(type(vowels))
print(vowels.items())
for i, j in vowels.items():
    print(i, "value is ", j )


print()
vowels = {'a', 'e', 'i', 'o', 'u'}
print(type(vowels))
print(vowels)
print()
print("======================================")
for i in range(2):
    print()

# ================================ Lets talk about tuple here ===================================


# Tuples are immutable, if the data in your structure never changes put it in a tuple.
print()
vowels1 = ('a', 'e', 'i', 'o', 'u')
#vowels1[2] = 'I'  # it throws an error because the data stored in a tuple should not be changed at all.
print(vowels1)


