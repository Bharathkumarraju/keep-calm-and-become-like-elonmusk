import requests
import json

url = ('http://google.com')

output = requests.get(url)

print("")
print(len(output.content))
print("\n"*2)
print(output.content)
print("")
print("\t"*2, output.status_code)
print("\n"*3)

urls = ('http://google.com', 'http://twitter.com')

for url in urls:
    print(url)

print("")

for resp in [ requests.get(urlz) for urlz in urls]:
     print(len(resp.content), '-->', resp.status_code, '-->', resp.url)

print("\n"*3)
