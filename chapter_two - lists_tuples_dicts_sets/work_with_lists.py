# which ones to store in lists
# For example Month's worth of daily temperature readings- string these values in list makes perfect sense

# you can create list dynamically in the program or statically


prices = []

temps = [ 32.012, 212.908, 0.001, -1.098, -9.098, 45.09876, 100.9872]

words = [ 'hello', 'doctor']

car_details = ['Toyota', 'BMW', 'TESLA', 2.091, 1e335353454029402384]

everything = [ prices, temps, words, car_details]

print()
print(everything[3][2])


odds_and_ends = [ [1, 2, 3], ['a', 'b', 'c'], ['one', 'two', 'three'] ]
print()
print(odds_and_ends[2][2])
print()

vowels = ['a', 'e', 'i', 'o', 'u']

word = "srianjaneyam prasanna anjaneyam prabha divya kaayam"

print(word)

for i in word:
    if i in vowels:
        print(i)

# how to display vowels found uniquely
print()
found = []
print(len(found))

print()
found.append('a')
print(len(found))
print(found)


if 'e' not in found:
    found.append('e')


if 'i' not in found:
    found.append('i')

if 'o' not in found:
    found.append('o')

if 'u' not in found:
    found.append('u')


print(found)

print()

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Sri anjaneyam rama lokshmana janaki jai bholo hanumanuki"
get_word = input("Please provide a word to search for vowels")
found = []
for letter in get_word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(found)
            print()
for j in found:
    print(j)


# list methods like append we have remove,pop,extend,insert and many more :)



multi_list = [11, 12.0, 99.90, 203.90, 'hello']

multi_list.remove('hello')
print()
print(multi_list)

multi_list.remove(99.90)
print()
print(multi_list)


# How to remove from a specific index slot use pop() method

multi_list.append('bk')
print(multi_list)

multi_list.pop(2)
print()
print(multi_list)

multi_list.pop()
print(multi_list)

multi_list.extend(["hanuman", "Raam", "lakshman", 18])
print()
print(multi_list)

multi_list.insert(1, "11 and half")
print()
print(multi_list)


multi_list.insert(0, "10 and half")
print()
print(multi_list)















