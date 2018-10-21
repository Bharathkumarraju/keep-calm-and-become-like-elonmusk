try:
    with open('anjaneyam.json') as hanuman:
        for i in hanuman:
            print(i)
except Exception as err:
    print("Error is: ", str(err))