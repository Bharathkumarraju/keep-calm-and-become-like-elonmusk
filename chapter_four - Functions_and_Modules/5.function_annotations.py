# Annotations are informational
# we are stating that word argument is expected to be a string
# we are stating that the function returns a set to its caller.

def search_for_vowels(word:str) -> set:
    """Returns any vowels found in specified word"""
    vowels=set('aaeeiioouu')
    return print(vowels.intersection(set(word)))

search_for_vowels('hello amma ')

print()

print(help(search_for_vowels))