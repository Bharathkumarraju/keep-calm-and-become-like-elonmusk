# Convert Don't Panic sentence to the on top

phrase = "Don't  panic!"
plist = list(phrase)
print()
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

print(plist)
plist.pop(0)
print(plist)


plist.remove("'")
print(plist)
print()
print()

#swap confuses bit

plist.extend([plist.pop(), plist.pop()])
print(plist)

plist.insert(2,plist.pop(3))

print(plist)

plist.pop(4)
print(plist)

new_phrase = ''.join(plist)
print(new_phrase)