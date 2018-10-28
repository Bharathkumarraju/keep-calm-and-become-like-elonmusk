import csv

with open('hanuman.csv') as lines:
    print(lines.read())
print("")

with open('hanuman.csv') as lines1:
    for i in csv.reader(lines1):
        print(i)
print("")

# using csv lets convert list to dictionary
with open('hanuman.csv') as lines2:
    for i in csv.DictReader(lines2):
        print(i)
print("")
