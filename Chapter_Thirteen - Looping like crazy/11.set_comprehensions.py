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
