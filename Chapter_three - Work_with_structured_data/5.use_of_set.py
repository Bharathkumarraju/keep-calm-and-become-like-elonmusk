# Sets don't allow duplicates
'''

sets are easy to spot in code, collection of objects are separated from one another by commas ans surrounded by curly braces

'''

#Creating set called vowels

vowels = {'a', 'a', 'e', 'i', 'o', 'e', 'e', 'o', 'i', 'u', 'u', 'o', 'e'}
print()

for i in vowels:
    print(i)
print()
print(vowels)

print()
print("Converting set as list")
print()
vowelslist = list(vowels)

print(vowelslist)

for i in vowelslist:
    print(i)


