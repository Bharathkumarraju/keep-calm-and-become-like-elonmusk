"""

Context management protocol expects to provide the __init__ __enter__ __exit__
1.  __init__ to per form initialization if needed.
2.  __enter__ to do any setup
3.  __exit__ to do any teardown

"""

print("")
with open('todo.txt') as tasks:
    for list_tasks in tasks:
        print(list_tasks, end='')
print("")

