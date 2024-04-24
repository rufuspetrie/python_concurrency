import threading
import time
from timeit import default_timer as timer

def thread_a():
    print("Thread A starting...")
    print("Thread A is calculating...")
    time.sleep(2)
    print("Thread A is calculating...")
    time.sleep(2)

def thread_b():
    print("Thread B starting...")
    print("Thread B is calculating...")
    time.sleep(5)
    print("Thread B is calculating...")
    time.sleep(5)

thread_1 = threading.Thread(target = thread_a)
thread_2 = threading.Thread(target = thread_b)
start = timer()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(f"Took {timer() - start:.2f} seconds.")
print("Done.")