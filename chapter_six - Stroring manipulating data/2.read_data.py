tasks=open('todos.txt')
# Print by default displays a new line. Telling print to not to display the newline with below
for i in tasks:
    print('\t'*9, i, end='')

tasks.close()


# Most programmers use 'with' statement while doing file operations that is open read/write close
# the beauty of 'with' statement is that it is smart enough to close files automatically when with block ends
# more importantly 'With' statement conforms to a coding convention built into python called the context management protocol

with open('todos.txt') as lines:
    for i in lines:
        print('\t'*18, i, end='')

