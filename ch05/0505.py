import threading
import requests
import time

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None

    def run(self):
        res = requests.get(self.url)
        self.result = f"{self.url}: {res.text}"

# ?sleep= specifies a delay for the request
urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
]

t0 = time.time()
threads = [MyThread(url) for url in urls]
for thread in threads: thread.start()
for thread in threads: thread.join()
for thread in threads: print(thread.result)
print(f"Took {time.time() - t0:.2f} seconds")
print("Done")