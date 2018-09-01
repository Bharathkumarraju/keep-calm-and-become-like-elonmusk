'''
Python's for loop understands lists, When provided with any list
for loop knows where the start of the list is
for loop knows how many objects the list contains
for loop knows where the end of the list is
you never have to tell the for loop any of this, as it works it out for itself.
'''

hanuman_bhajrangh = "jaya raaama, janaki pathi"

characters = list(hanuman_bhajrangh)

for letters in characters:
    print('\t \t', letters)
print()
print()
# Python's multiplication operator( * )


for char in characters[:11]:
    print('\t'*3, char)
print()
for char in characters[-5:]:
    print('\t'*5, char)
print()
for char in characters[13:19]:
    print('\t'*7, char)
print()








