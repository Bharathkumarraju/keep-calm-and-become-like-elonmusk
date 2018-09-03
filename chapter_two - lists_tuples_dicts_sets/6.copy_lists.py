first = [1, 2, 3, 4, 5]

second = first

second.extend([6, 7, 8])
print()

print(second)

print()

print(first)

# It is very strange , when you append an object to second list it also appends to first as well
# It is too bad behaviour

# So always use the copy method to copy the lists

third = second.copy()

print()
print(third)
third.extend([9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
print()
print(third)

saying = "Don't Panic!"

letters = list(saying)

print(letters)

print(letters[0])

print(letters[-1])

print(letters[-12])
first_letter = letters[0]
last_letter = letters[-1]
for i in range(2):
    print()
print(first_letter)
print(last_letter)


#Like range  Lists also takes the START, STOP and STEP arguments like below

print(letters[0:9:2])

#START with 0 index and STOP with index value 10(but not included), STOP value always not included and the every 2nd letter to step

print(letters[3:]) # Prints all letters except first 3 START from index value 3

print(letters[:10]) # STOP value is 10 index value, prints till 10 index but should not include 10th index

print(letters[::2])  # STEP value is 2 means prints every second letter



