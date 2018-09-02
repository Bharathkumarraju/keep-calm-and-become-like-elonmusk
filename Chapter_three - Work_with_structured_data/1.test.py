import os
for i in range(5):
    print()
print('\t'*18, "Hello world lets welcome Jai bhajrangbhali")

for i in range(5):
    print()

# How to define a Dictionary

person = { 'Name':  'Bharathkumar', 'Gender': 'Male', 'Occupation': 'Cloud Platform Engineer', 'Home Planet': 'Venus'}

for i in range(3):
    print('\t'*9, )


print(person)


# How to define a list

phrase = "Rama dootha athulitha, bala dhaama , anjani puthra pavana sutha nama"

hanumanlist = list(phrase)

print(hanumanlist)

hanumanlist_phrase = ''.join(hanumanlist)

print()
print(hanumanlist_phrase)


person1 = {'Conutry': 'India', 'State': 'TamilNadu', 'District': 'Chennai', 'city': 'chennai'}

print()
print(person1)



person2 = {
         'Name': 'Jai Bhajrang Bhali',
         'Residence': 'Heaven',
         'Country': 'Mangolia',
         'Age': 'Inifinity'
}

print()
print(person2)

print()
print(person2['Age'])   # It prints the value of the  key i.e. Age from the person2 dictionary
print(person1['State']) # It prints the value of the key  i.e. State from the person1 dictionary
print(person['Home Planet']) # It prints the value of the key i.e. Home Planet from the person dictionary
print()


person2['Inspirational person'] = 'Elon musk'

print(person2)

person2['Favourite Programming language'] = 'Python programming language'

print(person2)

print(len(person2))



print(person2['Favourite Programming language'])
print('\t'*18, person2['Inspirational person'])





