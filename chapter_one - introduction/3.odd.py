from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
         23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
         43, 45, 47, 49, 51, 53, 55, 57, 59]
for i in odds:
    print(i)

right_now_minute = datetime.today().minute

current_time = datetime.today().time()

print("current time is now")
print(current_time)

print("")
print(right_now_minute)

if right_now_minute in odds:
    print("Current minute is Odd")
else:
    print("Current minute is even")


