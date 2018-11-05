import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return  datetime.datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

print("")
print(convert2ampm('19:55'))
print(convert2ampm('21:45'))
print("")

try:
    with open('hanuman.csv') as data:
        data.readline()
        flights = {}
        for i in data:
            k, v = i.strip().split(',')
            flights[k] = v
        pprint.pprint(flights)
        print()
        flights2 = {}
        for k, v in flights.items():
            flights2[convert2ampm(k)] = v.title()
        pprint.pprint(flights2)
except Exception as err:
    print("The error is %s" % err)
print()

# Now convert dictionary to lists
flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))
print(flight_times)

destinations = []
for dest in flights.values():
    destinations.append(dest.title())
print(destinations)