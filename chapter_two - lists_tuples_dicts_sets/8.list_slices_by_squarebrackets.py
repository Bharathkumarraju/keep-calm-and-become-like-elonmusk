bkrword = "Don't panic!"

bkrwordlist = list(bkrword)

print(bkrwordlist)

newbkrword1 = ''.join(bkrwordlist[1:3])
print(newbkrword1)

new_phrase = newbkrword1 + ''.join([bkrwordlist[5],bkrwordlist[4],bkrwordlist[7],bkrwordlist[6]])
print()
print(bkrwordlist)
print(new_phrase)


