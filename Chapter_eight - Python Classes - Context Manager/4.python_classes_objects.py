
#classes start with class keyword


class CountFromBy:
    def __init__(self, v:int=0, i:int=1) -> None:
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> str:
        return str(self.val)

# Create an objects from the created class

hanuman = CountFromBy(100, 10)  # Creating an object called hanuman
print("")
print(hanuman)
print(type(hanuman))
print(id(hanuman))
print(hex(id(hanuman)))

print("")
print(hanuman.val)
print(hanuman.incr)


print(hanuman.val)
print(hanuman.incr)

print(hanuman.val)
print(hanuman.incr)

print("")

# Calling the increase method

hanuman.increase()
print(hanuman.val)
print(hanuman.incr)

print("")
print(hanuman.val)
print(hanuman.incr)
print("")
print("")
hanuman.increase()
print(hanuman.val)
print(hanuman.incr)

print("")
print(hanuman.val)
print(hanuman.incr)