word="bottles"

print("")

for i in range(99, 0, -1):
    print(i,word, "of beer on the wall")
    print("take one down")
    if i == 1:
        print("No more bottles of beer on wall")
    else:
        j = i - 1
        if j == 1:
            word="bottle"
        print(j,word, "of beer on the wall")
    print()

# How range really works

print(list(range(5)))

print(list(range(5, 10)))

print(list(range(0, 10, 2)))

print(list(range(10, 0, -2)))

print(list(range(99, 0, -1)))

