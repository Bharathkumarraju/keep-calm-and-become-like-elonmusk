book = "The stephen Hawking's guide to the galaxy"

booklist = list(book)

print()
print(booklist)

print(booklist[0:3])


print(''.join(booklist[0:3])) # converts lists as string

#converts list to a string
bookstring = ''.join(booklist)
print(bookstring)
# How to convert list to a string ''.join(list)

print(''.join(booklist[-6:]))

backwards = booklist[::-1]

print()
print(backwards)
print(''.join(backwards))

every_other = booklist[::2]
print(every_other)
print(''.join(every_other))

print(''.join(booklist))
print(''.join(booklist[4:14]))
print(''.join(booklist))
slice_list = ''.join(booklist[:14:-2])
print(slice_list)





