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

print("\t"*9)
print("\t"*18)
print("\t"*36)

# how to get times and destinations separately

flight_timez=[]

for i in flights.keys():
    flight_timez.append(i)
print(flight_timez)
print("\t"*90)


flight_timezz=[]
for i in flights.keys():
    flight_timezz.append(convert2ampm(i))
print(flight_timezz)
print("\t"*199)
print("")


flights_destinations=[]
for i in flights.values():
    flights_destinations.append(i)
print(flights_destinations)

print("")
print("")

flights_destonationzz=[]
for i in flights.values():
    flights_destonationzz.append(i.title())
print(flights_destonationzz)
print("")
print("")




