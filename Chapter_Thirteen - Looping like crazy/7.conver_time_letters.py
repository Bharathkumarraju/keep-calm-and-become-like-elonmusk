import pprint
print("")
try:
    with open('hanuman.csv') as god:
        god.readline()
        flights = {}
        for i in god:
            k, v = i.strip().split(',')
            flights[k] = v
        pprint.pprint(flights)
except Exception as err:
    print("The error is %s" % err)


