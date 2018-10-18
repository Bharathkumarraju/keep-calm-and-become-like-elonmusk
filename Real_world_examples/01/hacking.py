import requests
import urllib
import json
import string
import os
import random


chars =  string.ascii_letters + string.digits + '!#%$^&*@()'
random.seed = (os.urandom(1024))
print(chars)

print("")
print("")

url  = 'https://accounts.craigslist.org/login?lang=en&cc=us'




#names = json.load(open('names.json').read())
names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    username = name.lower() + name_extra +'@yahoo.com'
    #print(username)
    password = ''.join(random.choice(chars) for i in range(8))
    #print(password)

    requests.post(url, allow_redirects=False, data={
        'inputEmailHandle': username,
        'inputPassword': password
    })

    print('sending username %s and sending password %s' %(username, password))