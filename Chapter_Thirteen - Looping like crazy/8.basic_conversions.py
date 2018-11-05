s = "This is my first python's coversion program"
print("")
print(s)
print("")
print(s.title())
print("")

# how to use datetime module with string format specifiers

from datetime import datetime

def convert2ampm(time24: str) -> str:
    return print(datetime.strptime(time24, '%H:%M').strftime('%I:%M%p'))

convert2ampm('19:00')

convert2ampm('21:00')

