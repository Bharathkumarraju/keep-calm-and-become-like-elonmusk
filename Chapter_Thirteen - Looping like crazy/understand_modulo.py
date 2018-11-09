x = [1, 2, 3, 4, 5, 6, 7, 8]
y = []
z = []
for i in x:
    print(i%2)

for i in x:
    if i%2:
        y.append(i)
    print(y)

print("")
print("")

for i in x:
    if not i%2:
        z.append(i)
    print(z)
print("")
print("")
