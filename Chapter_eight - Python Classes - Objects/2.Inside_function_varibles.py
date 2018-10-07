def soundbite(from_outside):
    inside = "James"
    outside= from_outside
    print(from_outside, inside, outside)

name = "Bond"
soundbite(name)

#Varibles from the inside the function not accessible outside
print(inside)
print(outside)
print(from_outside)