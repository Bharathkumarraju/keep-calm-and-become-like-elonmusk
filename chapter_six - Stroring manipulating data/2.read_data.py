tasks=open('todos.txt')
# Print by default displays a new line. Telling print to not to display the newline with below
for i in tasks:
    print('\t'*9, i, end='')

tasks.close()



