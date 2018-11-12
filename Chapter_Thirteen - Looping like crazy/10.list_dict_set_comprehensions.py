data = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for i in data:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("")
print("the even numbers are",even)
print("The odd numbers are",odd)

print("")

even1=[]

for i in data:
    if not i%2:
        even1.append(i)
print(even1)
print("")

odd1=[]
for i in data:
    if i%2:
        odd1.append(i)
print(odd1)
print("")
print("begining of comprehension")
print("\n"*2)


print_even = [ i for i in data if not i%2 ]
print(print_even)


print_odd = [i for i in data if i%2]
print(print_odd)

print("\n"*2)


data1 = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for i in data1:
    if isinstance(i, str):
        words.append(i)
print(words)

print("\n"*3)
words_comprehension = [ i for i in data1 if isinstance(i, str) ]
print(words_comprehension)


# Title case comprehension

data2 = list('so long and thanks for the all the fish'.split())
print(data2)
print("")
for i in data2:
    print(i)

print("\n"*2)
title = []
for i in data2:
    title.append(i.title())
    print(title)

print("\n"*3)
print("The more sophisticated list comprehension ")
print("")
print_title = [ i.title() for i in data2 ]
print(print_title)
print("\n"*2)