'''

you can mix and match python built-in data structures that is lists,dictionaries,sets,tuples

you can use as

lists of lists, lists inside dictionaries , lists inside sets , lists inside tuples, dictionary of dictionaries etc...

any of the built-in data structures can be stored in the any other built-in data structure

'''

# How to use dictionary of dictionaries

print()
people = {}
print(type(people))


people['Ford'] = {'Name': 'henry Ford',
                  'Occupation': 'CEO',
                  'Gender': 'Male',
                  'Age': '101',
                  'Home planet': "Heavenly mars"}
print()
print(people.items())


people['Hawkings'] = {'Name': 'Stephen hawkings',
                  'Occupation': 'Scientist',
                  'Gender': 'Male',
                  'Age': '99',
                  'Home planet': "Venus"}

people['Musk'] = {'Name': 'Elon Musk',
                  'Occupation': 'Programmer',
                  'Gender': 'Male',
                  'Age': '45',
                  'Home planet': "Heavenly earth"}

people['Ramanujan'] = {'Name': 'Srinivasa Ramanujan',
                  'Occupation': 'Mathematician',
                  'Gender': 'Male',
                  'Age': '201',
                  'Home planet': "Jupiter"}

people['Gates'] = {'Name': 'Bill Gates',
                  'Occupation': 'Charity person',
                  'Gender': 'Male',
                  'Age': '51',
                  'Home planet': "Saturn"}


print()

print(people.items())

print()
print(people['Gates'])


print()

print(people)
print()
print()

# Pretty-Printing complex data structures
# import the pprint module and then import the pprint function to do the work

import pprint

pprint.pprint(people)

print()
pprint.pprint(people)
print()

print(people['Ramanujan']['Occupation'])

print(people['Gates']['Home planet'])

print(people['Musk']['Name'])

print(people['Ford']['Age'])

print(people['Hawkings']['Gender'])
print()




