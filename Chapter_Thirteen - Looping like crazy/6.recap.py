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
#        print(flights)
except Exception as err:
    print("the error is %s" % err)

# strip removes the whitespace from the beginning and end of an existing string

# strip() - Let's remove the unwanted trailing newline from raw data using i.strip().spilt(',')