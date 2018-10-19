import requests
import os
import string
import random
import json

names = json.loads(open('names.json').read())

for i in names:
    print(i)

chars = string.ascii_letters + string.digits + '!@#$%^*()+'

print(chars)

url = 'http://www.esevaonline.ap.gov.in/epay/ConsData.jsp'

list1 = ["hanuman", "anjaneya", "bhajarang", "Maharaj-ji"]

delimiter = '_/\_'
joins = ''.join(list1)
joining1 = delimiter.join(list1)
print(joining1)

requests.post(url,allow_redirects=False,
    data={
    'userIdTxt': 'raju123456',
    'pwdTxt': 'helloootest123'
         }
)


name = "jaiHanumaaaaaan"
name_extra = ''.join(string.digits)
name_random_extra = ''.join(random.choice(string.digits) for i in range(5))
full_name = name + name_random_extra
print("")
print(full_name)

password = ''.join(random.choice(chars) for i in range(5)) + name_random_extra

print(password)

names1=json.loads(open('names.json').read())

for namez in names1:
    username = namez.lower() + name_random_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(9)) + name_random_extra
    requests.post(url, allow_redirects=False, data={
        'userIdTxt': username,
        'pwdTxt': password
    })
    print('sending the username %s and sending the password %s' %(username, password))



