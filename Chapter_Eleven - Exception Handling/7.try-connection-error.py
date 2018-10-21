try:
    raise ConnectionError('Whoops')
except ConnectionError as err:
    print('Got:', str(err))

