word = "bottles"
print()
print(word)

print(list(range(100, 0, -1)))

for beer_num in range(100, 0, -1):
    print(beer_num,word, "of beer on the wall")
    print("take one down")
    print("pass it on")
    if beer_num == 1:
        print("No more bottle of beer on the wall")
    else:
        new_num = beer_num - 1
        print(new_num)
        if new_num == 1:
            word = "bottle"
        print(new_num,word, "beer on the wall")
    print()





