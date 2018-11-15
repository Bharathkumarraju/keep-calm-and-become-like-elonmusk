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