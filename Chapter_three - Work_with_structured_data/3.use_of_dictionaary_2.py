vowels = ['a', 'e', 'i', 'o', 'u']
for i in vowels:
    print(i)

get_the_word = input("Please enter the word in order to find out the vowels in it")
found = {}  #Initializes an empty dictionary
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
print(found)

for i in get_the_word:
    if i in vowels:
        found[i] += 1
        print(found)
print()
for k, v in sorted(found.items()):
    print(k, 'is found in', v, 'times')



fruits = {}

fruits['apple'] = 10
print()

status = 'apple123' in fruits
print()
print(status)  # It will prints True and False based on the

print()
for i in fruits.items():
    print(i)

if 'bananaas' in fruits:
    fruits['bananaas'] += 12
else:
    fruits['bananaas'] = 1
print()
print(fruits)

if 'bananaas' in fruits:
    fruits['bananaas'] += 17
else:
    fruits['bananaas'] += 2
print()
print(fruits)

if 'sapota' not in fruits:
    fruits['sapota'] = 0
    fruits['sapota'] += 1
    print(fruits)
print()

#use setdefault method

fruits.setdefault('oranges', 1)
fruits['oranges'] += 5
print(fruits)
print()

stausss = 'watermelon' in fruits
print()
print('\t'*5 , stausss)
print()












