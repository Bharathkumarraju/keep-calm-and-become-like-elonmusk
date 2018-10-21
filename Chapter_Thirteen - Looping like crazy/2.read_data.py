import os
import csv
try:
    os.chdir('/Users/bharathdasararaju/PycharmProjects/keep-calm-and-become-like-elonmusk/Chapter_Thirteen - Looping like crazy')
    with open('hanuman.csv') as data:
        print(data.read())
except Exception as err:
    print('The error is %s' % err )

print("")
print("")

try:
    os.chdir('/Users/bharathdasararaju/PycharmProjects/keep-calm-and-become-like-elonmusk/Chapter_Thirteen - Looping like crazy')
    with open('hanuman.csv') as data:
        for i in csv.reader(data):
            print(i)
except Exception as err:
    print("the error is %s" % err)

try:
    os.chdir('/Users/bharathdasararaju/PycharmProjects/keep-calm-and-become-like-elonmusk/Chapter_Thirteen - Looping like crazy')
    with open('hanuman.csv') as data:
        for i in csv.DictReader(data):
            print(i)
except Exception as err:
    print("the error is %s" % err)



