import pprint

print("Conversion python")
print("")
try:
    with open('hanuman.csv') as data:
        data.readline()
#        print(ignore)
        flights = {}
        for line in data:
            k, v = line.split(',')
#            print(k, v)
            flights[k] = v
            pprint.pprint(flights)
except Exception as err:
    print("Error message is %s " %err)
