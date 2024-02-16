import requests

def ping(url):
    res = requests.get(url)
    print(f"{url}: {res.text}")

# The httpstat site simply returns the status code associated with each page
urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]

for url in urls:
    ping(url)
print("Done")