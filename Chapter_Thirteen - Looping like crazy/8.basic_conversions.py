import pprint
from datetime import datetime

s = "This is my first python's coversion program"
print("")
print(s)
print("")
print(s.title())
print("")

# how to use datetime module with string format specifiers



def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

convert2ampm('19:00')
convert2ampm('21:00')

print("")
print("")

try:
    with open('hanuman.csv') as data:
        data.readline()
        flights = {}
        for i in data:
            k, v = i.strip().split(',')
            flights[k] = v
    pprint.pprint(flights)
    print("")
    flights2 = {}
    for k, v in flights.items():
        flights2[convert2ampm(k)] = v.title()
    pprint.pprint(flights2)
except Exception as err:
    print("Error is %s" % err)

print("")
print("")