vowels = [ 'a', 'e', 'i', 'o', 'u']
find = []  # Initialize an empty list
get_word=input("Please enter a word to find out the vowels in it")
print()

for i in get_word:
    if i in vowels:
        if i not in find:
            find.append(i)
        print(find)

for j in find:
    print(j)



print(get_word)
print(len(find))

# Initialize an empty dictionary
found = {}


print()
print(found)
print(len(found))

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

print()
print(found)
print(len(found))

print(found['e'])

print(found['e'])

found['e'] = found['e'] + 18
found['e'] += 18
print()
print(found['e'])
print()
print(found)
print()

found['u'] += 9

print(found['u'])

print(found)

found['u'] -= 6
found['e'] -= 27

print()
print(found)
print()
for i in found:
    print(i,",it's found in",found[i],"time's .")

print()

# How to make ordered dictionary using the pythons built-in-function i.e. sorted

for i in sorted(found):
    print(i, 'is found in', found[i], 'times')

print()

# The best way to use the dictionary key values is to use the items method like below

for a, b in found.items():
    print(a, 'is found in', b, 'times')

# Use the sorted method to make sure that it prints in correct order
for i in range(2):
    print()

for i, j in sorted(found.items()):
    print(i, "is found in", j, "times.")








