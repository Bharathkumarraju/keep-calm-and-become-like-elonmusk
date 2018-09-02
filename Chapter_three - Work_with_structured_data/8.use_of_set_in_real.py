vowels = ['a', 'e', 'i', 'o', 'u']

# =============================== use of lists =========================================
get_the_word = input("Please enter word to find vowels in it using python lists")
print()

found = []
for i in get_the_word:
    if i in vowels:
        if i not in found:
            found.append(i)
print(found)
for i in sorted(found):
    print(i)



# =============================== use of dictionaries ===================================

get_the_word = input("Please enter the word in order to find out the vowels in it using python dictionaries ")

found = {}

print()
for i in get_the_word:
    if i in vowels:
        found.setdefault(i, 0)
        found[i] += 1

for a, b in found.items():
    print(a, "found in", b, "times")


# ============================== use of sets =============================================
get_the_word = input("Please enter the word in order to find out the vowels in it using the python sets ")
vowels = set('aeiou')

found = vowels.intersection(set(get_the_word))
print((found))
print()
for i in sorted(found):
    print(i)

