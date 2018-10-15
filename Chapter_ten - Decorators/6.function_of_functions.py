msg = "Hello from the Sri Anjaneyam Prasanna Anjaneyam"
print(id(msg))
def hello():
    print(msg)    
hello()   
print(type(msg))
print(type(hello))
print(id(hello))
print("")
print("")
# How to invoke a passed function
# How to pass a function object to a function and how to invoke it
def apply(func: object, value=object) -> object:
    return print(func(value))

apply(print, 9)
apply(type, 9)
apply(id, 9)

apply(len, 'Sri anjaneyam')
apply(type, apply)

# Functions can be nested inside functions
# How to define a function inside a function, nested function (or) inner function
# Nested function can be returned from the outer enclosing function
print("")

def outer():
    def inner():
        print('This is inner')
    print('This is outer, invoking inner')
    inner()
    
outer()

print("")

def outer2():
    def inner2():
        print('This is inner 2')
    print('This is outer 2, Returning inner2')
    return inner2

i = outer2()
print(type(i))
i()
print("")
print("")
# Create a function that accepts the any number of arguments or any type of arguments
# *args is for the list
def hanumanfunc(*args):
    for a in args:
        print(a, end='')
    if args:
        print()

hanumanfunc(10)
hanumanfunc()
hanumanfunc(10, 20, 30, 40, 50, 60)
hanumanfunc(1, 'two', 3, 'Seven', 9)

values_dict={"user": "bharath", "password": "Hanuman123"}
values_dict2={"a": 1, "b": 20}
values_list=[1, 2, 8, 18, 19, 20]
hanumanfunc(values_list)
hanumanfunc(*values_list)

'''
hanumanfunc(values_dict)
hanumanfunc(*values_dict) # :) It is just taking keys of dictionary and appending key=user value=bharath and key=password value=Hanuman123
'''
print("")
# Let's define a function which accepts any number of dictionaries of arguments
# **kwargs

def hanumanfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end='')
    if kwargs:
        print()
        
#hanumanfunc2(values_dict) --> won't work
hanumanfunc2(a=10, b=78, c=90, d=109)
hanumanfunc2()
hanumanfunc2(a=10, b=20)
#hanumanfunc2(values_dict) --> won't work
hanumanfunc2(**values_dict) # Works like a Charm
hanumanfunc2(**values_dict2) #Works like a charm


dbconfig = {
    'host': '127.0.0.1',
    'user': 'wordsearch',
    'password': 'wordsearchpassword',
    'database': 'wordsearchlogDB'
}

hanumanfunc2(**dbconfig)










