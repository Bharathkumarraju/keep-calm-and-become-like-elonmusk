def double(arg):
    print("before the value is ", arg)
    print("")
    arg = arg * 2
    print("after the value is", arg)
    print("")
    print("")


double(100)
double("Sri Anjaneyam")
double("Jai Bhajrang Bhali")
numbers=[10, 18, 20]
double(numbers)

def spaces(num):
    for i in range(num):
        print("")
spaces(9)
def change(arg):
    print("before it is ", arg)
    arg.append('More data')
    print("after it is", arg)

#change("Sri anjaneyam")
change(numbers)
