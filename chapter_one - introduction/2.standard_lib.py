'''

The standard library is the jewel in Python’s crown, supplying reusable modules that help you with
everything from, for example, working with data, through manipulating ZIP archives, to sending emails,
to working with HTML.

The standard library even includes a web server, as well as the popular SQLite database technology.

'''

from datetime import datetime
from os import getcwd
from json import decoder
from sys import platform
from enum import unique
from random import random
from time import get_clock_info
import os
import sys
import datetime
import time
import html

current_date =  datetime.date.today()
current_time = datetime.date.today().ctime()

print("")
print(current_time)

print("")
print(current_date)

print("")
current_working_directory = getcwd()

print(current_working_directory)

print("")
current_platform = platform
print(current_platform)

print("")
print("Print All SYS standard lib functions")
print(sys.platform)
print(sys.version)


print("")
print("Print All OS standard lib functions")
print(os.environ)
print(os.getcwd())
print(os.getenv('HOME'))

print("")
print("dattime lib")
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.today().isoformat())


print("")
print("time lib")
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))

print("HTML Standard library")
print(html.escape("This HTML fragment contains a <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))

'''
As the standard library is so rich, the thinking is all you need to be immediately productive with
the language is to have Python installed.
'''

print(datetime.date.today().isocalendar())

now_date = datetime.datetime.today()
current_minute = now_date.minute

print(current_minute)
print(now_date)


even = [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 42, 44, 46, 48, 50, 52, 54, 56, 58 ]
for i in even:
    print(i)

print("")
print("")
print(current_minute)
if current_minute in even:
    print("We are in the even minute")
else:
    print("We are int he Odd minute")

print("")
current_day = time.strftime("%A")
print(current_day)

if current_day == "Monday":
    print("WORK WORK")
elif current_day == "Tuesday":
    print("German class")
elif current_day == "Wednesday":
    print("WORK WORK")
elif current_day == "Thursday":
    print("Learn Python")
elif current_day == "Friday":
    print("learn shell")
elif current_day == "Saturday":
    print("Sleep")
elif current_day == "Sunday":
    print("Work again")
else:
    print("No fucking day is available")


