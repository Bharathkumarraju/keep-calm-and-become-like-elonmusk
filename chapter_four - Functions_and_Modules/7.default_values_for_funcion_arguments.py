# Specify default values for function arguments

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ search for specified letters in the provided phrase and  specifying default value for letters"""
    return print(set(letters).intersection(set(phrase)))
print()
search4letters("Raju")

search4letters("Raju", "HaRe Rama Hare Krisha u")



