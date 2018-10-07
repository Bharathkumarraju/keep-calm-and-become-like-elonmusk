
#classes start with class keyword

class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> str:
        return str(self.val)

print("")
# Create an objects from the created class
k = CountFromBy()
print(k)
k.increase()
print(k)

l = CountFromBy(100)
print(l)
l.increase()
print(l)

m = CountFromBy(100, 10)
print(m)
m.increase()
print(m)

n = CountFromBy(i=15)
print(n)
n.increase()
print(n)




