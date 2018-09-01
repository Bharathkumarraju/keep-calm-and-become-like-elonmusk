bkword = "Don't panic!"


bkwordlist = list(bkword)

print()
print(bkwordlist)

for i in range(4):
    bkwordlist.pop()
print(bkwordlist)

bkwordlist.extend([bkwordlist.pop(),bkwordlist.pop()])
print()
print(bkwordlist)
bkwordlist.remove('\'')
print(bkwordlist)
bkwordlist.pop(0)
print(bkwordlist)
bkwordlist.insert(2,bkwordlist.pop(3))
print()
print(bkwordlist)

print(''.join(bkwordlist))



