import sys
"""
A standard library comes with a module called sys that provides access to the interpreters internals
one such function is exc_info()
exc_info() returns three values tuple
1. First value indicates the exceptions type
2. Second details the exceptions value
3. Third contains the traceback object that provides the access to the traceback message
"""

sys.exc_info()
print("")
print(sys.exc_info())



try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)



