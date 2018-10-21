"""
Extend the except exception statement with the 'as' keyword which allows
Current exception object to a variable and create more informative error message

"""
try:
    with open('hanuman.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print("The data file is missing")
#except PermissionError:
#    print("Unable to read the files data")
#except:
#    print("Some other error occurred")
except Exception as err:
    print('The error occured is', str(err))




