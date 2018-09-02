vowels = ['a', 'e', 'i', 'o', 'u']
for i in vowels:
    print(i)

found = {}
get_the_word = input("Enter the word to calculate the vowels in it")

for i in get_the_word:
    if i in vowels:
        found.setdefault(i, 0)
        found[i] += 1
for a,b in sorted(found.items()):
   print(a, 'is found in', b, 'times')







