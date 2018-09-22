def search_for_vowels_from_the_phrase(phrase:str) -> set:
    """ Returns any vowels found in the phrase"""
    vowels=set('aaeeiioouuuu')
    return print(vowels.intersection(set(phrase)))

search_for_vowels_from_the_phrase("hello guys hw r u")

def spaces(howmany):
    for i in range(howmany):
        print()

spaces(5)

print(help(search_for_vowels_from_the_phrase))



spaces(2)
print("Sri ram jai ram jai jai ram. sri ram jai ram jai jai ram")
spaces(3)
print("sitha ranm jaya sitha ram")



def search4letters(phrase:str, letters:str) -> set:
    """Returns the set of 'letters' found in a 'phrase' """
    return print(set(letters).intersection(set(phrase)))

spaces(5)
search4letters('hello doctor', 'lo')
spaces(4)

print(help(search4letters))

spaces(2)

search4letters('Sri anjaneyam', 'BK')
spaces(1)