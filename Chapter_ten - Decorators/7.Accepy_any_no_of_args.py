def hanumansfunc(*args):
    for i in args:
        print(i, end='')
    if args:
        print()

def hanumansfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k, v, sep='->', end='')
    if kwargs:
        print()

def hanumansfunc3(*args, **kwargs):
    if args:
        for i in args:
            print(i, end='')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='--->', end='')
        print()

hanumansfunc3(1, 2, 3)
hanumansfunc3(a=10, b=20, c=30)
hanumansfunc3(1, 2, 3, a=10, b=20, c=30)
values = {'hanuman': 'chaleesa', 'Maharaj_ji': 'neemkaroli', 'Godofgods': 'Jaibhajranghali'}
hanumansfunc3(**values)
