def search4vowels(word):
    vowels = set('aeiouauiou')
#    get_word = input("Enter a word: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

def spaces(spaces):
    for i in range(spaces):
        print()



search4vowels('helloi')

spaces(5)

search4vowels('sri anjaneyam')

#search4vowels('sri anjaneyam', 'prasanna anjaneyam')







