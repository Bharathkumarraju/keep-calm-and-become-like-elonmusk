'''

lists are not good when you have a data as key/value pairs
like

Name: Bharath kumar
Gender: Male
Occupation: Researcher
Home Planet: Venus


'''

person = [ 'Name', 'Bharath kumar', 'Gender', 'Male', 'Occupation', 'Researcher', 'Home Planet', 'Venus']

for i in person:
    print('\t'*9, i)

# So here comes problem, that is we don't know which index persons name or persons gender or persons occupation
# In order to solve this we have another data structure called Dictionary.

print(''.join(person))
