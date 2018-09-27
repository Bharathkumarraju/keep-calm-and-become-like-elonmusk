def search4vowel(word:str) -> set:
    """This method find vowels in a specified word"""
    vowels = set('aeaeioiouu')
    return print(vowels.intersection(set(word)))
# caught = vowels.intersection(set(word))

print(help(search4vowel))

search4vowel("hello hw r u")


print("")
print("")

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """"""
    return print(set(letters).intersection(set(phrase)))

search4letters("hello hw r u")

print("")




