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

for spaces in range(5):
    print()



def word_search(hanuman_word):
    vow=set('aaeeiiooouu')
    return print(vow.intersection(set(hanuman_word)))

word_search('raju')

word_search('sky')
print()

# Recall the built-in data structures list, tuple, set, tuple
print()
# Lists
l = list()
print(l)
l = [1, 2, 3]
print(l)

print()
# Dictionaries
d = dict()
print(d)
d = { 'first': 1, 'second': 2, 'third': 3}
print(d)

print()
# sets
s = set()
print(s)
s = {1, 2, 3}
print(s)

print()
# tuples
t = tuple()
print(t)
t = (1, 2, 3)
print(t)

for i in range(5):
    print()

x=list()
print(x)

y=tuple()
print(y)

z=set()
print(z)

w=dict()
print(w)




