try:
    with open('hanuman.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print("The data file is missing")
except PermissionError:
    print("Unable to read the files data")


