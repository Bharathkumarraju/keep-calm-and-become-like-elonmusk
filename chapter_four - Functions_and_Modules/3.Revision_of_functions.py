vowels = set("aeioueioaiuoeaaaa")

for i in range(5):
    print()


print(type(vowels))
print()

print(vowels)


get_word = input("Please enter the word to find out the vowels in it: ")
found = vowels.intersection(set(get_word))
print("")
print(list(found))



def spaces(count):
    for i in range(count):
        print()

spaces(3)

print("hanuman")




# How to pass arguments to the function


def search_for_vowels(myword):
    """Display any vowels found in supplied word."""
    vowels1=set('aaeeiiiooouu')
    founded = vowels1.intersection(set(myword))
    print()
    print(founded)
    print()
    print(list(founded))

print()
search_for_vowels("hihe")
print()
search_for_vowels("Sri anjaneyam, prasanna anjaneyam Oum Bhajrang bhali")
print()

search_for_vowels('hello ellen')

