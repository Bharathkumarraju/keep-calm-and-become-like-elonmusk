def num_cubed(num):
    return num**3

print("")
print(num_cubed(3))
print("")
print("")

list_normal = [2, 3, 4, 5, 6, 7, 8, 9]
list_cubed = []

for num in list_normal:
    list_cubed.append(num_cubed(num))
    print(list_cubed)

print("")
print("")
#above 3 lines wrapped in single line as below

hanuman_list_cubed = [num_cubed(x) for x in list_normal]

print(hanuman_list_cubed)


# We have list_normal and list_cubed and hanuman_list_cubed, let's do magic with lambda
print("")
print("")

list_normal_new = [2, 3, 4, 5, 6, 7, 8, 9]
list_cubed_new = list(map(lambda x: x**3, list_normal_new))

print(list_cubed_new)
