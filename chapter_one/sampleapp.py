word="bottles"

print("")

for i in range(100, 0, -1):
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




