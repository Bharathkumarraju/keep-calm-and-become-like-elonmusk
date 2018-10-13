import os

CREDENTIALS_FILE = '~/.test123'
def read_credentials(file_name=os.path.expanduser(CREDENTIALS_FILE)):
    credentials = {}
    with open(file_name, 'r') as f:
        for line in f:
            credentials['user'], credentials['password'] = line.strip().split(':')
            print(credentials)
print("")
print("\t"*9, "hello")
read_credentials()

