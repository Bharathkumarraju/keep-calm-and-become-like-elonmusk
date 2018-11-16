import requests

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):  # For loop line with the generator
        yield len(resp.content), resp.status_code, resp.url

# don't use code like  return len(resp.content), resp.status_code, resp.url
# Instead of return statement use the yield statement especially designed for the Generators.