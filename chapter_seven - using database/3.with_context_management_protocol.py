def spaces(number):
    for i in range(number):
        print("")

spaces(9)
with open('todo.txt') as todos:
    for hanumans in todos:
        print(hanumans,end='')

spaces(3)
