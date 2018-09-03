vowels = set('aeiou')
word = 'hello'

# use the set method i.e. union
u = vowels.union(set(word))
print()
print(u)

print()

for i in u:
    print(i)

u_list = list(u)
sorted_u_list = sorted(list(u))

print()
print(u_list)

print()
for i in u_list:
    print(i)

print()

print(sorted_u_list)

print()

for i in sorted_u_list:
    print(i)
print()

# Use the set method i.e. difference

d = vowels.difference(set(word))
print()
print(d)
print()

for i in d:
    print(i)

# Use the set method i.e. intersection

i = vowels.intersection(set(word))

print()
print(i)

for j in i:
    print(j)
print()

