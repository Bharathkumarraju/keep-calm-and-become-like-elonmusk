import datetime
import time
import random

current_minute = datetime.datetime.today().minute

print(current_minute)
print("")
x = [1, 2, 3]

for i in x:
    print(i)


print("")
for i in 'Hi, guys hello!':
    print(i)

print("")
for i in range(5):
    print(i)

print("")

for i in range(3):
    print("Jai HANUMAN")

even = [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 42, 44, 46, 48, 50, 52, 54, 56, 58 ]

print("The current minute is ")
print(current_minute)

print((dir(random)))
print(random.randint(1,60))

for i in range(5):
    current_minit = datetime.datetime.today().minute
    if current_minit  in even:
        print("its even minit")
    else:
        print("its odd minit")
    wait_time = random.randint(1,60)
    print("The random wait_time is")
    print(wait_time)
    time.sleep(wait_time)







