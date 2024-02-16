import threading
import requests
import time

def ping(url):
    res = requests.get(url)
    print(f"{url}: {res.text}")

urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]

# Making web requests in sequence
t0 = time.time()
for url in urls:
    ping(url)
print(f"Sequential: {time.time() - t0:.2f} seconds\n")

# Because different servers are independent and most servers can handle
    # multiple requests simultaneously, it makes sense to parallelize
t0 = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target = ping, args = (url, ))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(f"Threaded: {time.time() - t0:.2f} seconds\n")