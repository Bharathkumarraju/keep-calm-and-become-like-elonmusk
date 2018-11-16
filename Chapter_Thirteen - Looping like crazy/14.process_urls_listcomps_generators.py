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

urls = ('http://google.com', 'http://twitter.com', 'http://facebook.com')

for url in urls:
    print(url)

print("")

# We can experience a noticable delay between entering for loop code and seeing the results
# When the results appear, they displayed in one go.
# This is because of the listcomp works through each of the urlz in the urls tuple before making any results available to the for loop.
# The outcome? you have to wait for your output.

for resp in [ requests.get(urlz) for urlz in urls]:
     print(len(resp.content), '-->', resp.status_code, '-->', resp.url)
print("\n"*3)
print("--------------------------------------------------------------------------------")
print("")

# Rewrite the above code using generator.
for response in (requests.get(url)for url in urls):
    print(len(response.content), '-->', response.status_code, '-->', response.url)

# Functions with Generators

from url_utils import gen_from_urls
urlss = ('http://google.com', 'http://twitter.com', 'http://facebook.com')
for resp_len, status, url in gen_from_urls(urlss):
    print(resp_len, status, url)

