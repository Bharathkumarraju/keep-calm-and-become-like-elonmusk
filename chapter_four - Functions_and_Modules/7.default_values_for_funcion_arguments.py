# Specify default values for function arguments

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ search for specified letters in the provided phrase and  specifying default value for letters"""
    return print(set(letters).intersection(set(phrase)))
print()
search4letters("Raju")

search4letters("Raju", "HaRe Rama Hare Krisha u")

search4letters("hanuman chaliesa", "chaleesa")

search4letters("Jai Bhajrang Bhalee")

print()
search4letters("India", "BKR")
print()






