'''

Reusing code is key to building a maintainable system

Take some lines of code give them a name and you have got a function.
Take a collection of functions and package them as a file and you have got a module.

'''

# Use def keyword to declare a function in python
# Functions introduce two new keywords: i.e. def and return
# Functions can accept argument data

def srianjaneyam():
   for i in range(5):
       print()
       print("SRI ANJANEYAM")

srianjaneyam()
print()
print(bool(0))
print()
print(bool(1))
print()

def search4vowels():
    vowels = set('aeiouaeouiiouaei')
    word = input('please enter a  word to find vowels in it: ')
    found = vowels.intersection(set(word))
    for i in found:
        print(i)

search4vowels()





