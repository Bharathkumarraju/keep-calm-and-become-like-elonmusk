print("All False evaluations")
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(''))
print(bool(None))
print(bool({}))
print()

print("All True evaluations")
print(bool(1))
print(bool(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000001))
print(bool(-1))
print(bool([1, 2, 3]))
print(bool({'a': 12, 'b': 43}))
print(bool('Panic'))
print()

def search_for_word(myword):
    vowels=set('aaeeiioouu')
    found = vowels.intersection(set(myword))
    for i in found:
        print(list(i))
    print()
    print(list(found))

search_for_word("roopa")
search_for_word("amma")


def search_the_word(bkword):
    vowels1=set('aiioooeeuua')
    founded=vowels1.intersection(set(bkword))
    return print(bool(founded))

search_the_word("123")

search_the_word("roopa")

search_the_word("bkr")

search_the_word("amma")

search_the_word("DSR")

search_the_word("Hyma")

search_the_word("arun")

