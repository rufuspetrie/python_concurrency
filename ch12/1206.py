import threading
import time
from timeit import default_timer as timer

def thread_a():
    print("Thread A starting...")
    print("Thread A waiting to acquire lock A.")
    lock_a.acquire()
    print("Thread A has acquired lock A, calculating...")
    time.sleep(2)
    print("Thread A waiting to acquire lock B.")
    lock_b.acquire()
    print("Thread A has acquired lock B, calculating...")
    time.sleep(2)
    print("Thread A releasing both locks.")
    lock_a.release()
    lock_b.release()

def thread_b():
    print("Thread B starting...")
    print("Thread B waiting to acquire lock A.")
    lock_a.acquire()
    print("Thread B has acquired lock A, calculating...")
    time.sleep(5)
    print("Thread B waiting to acquire lock B.")
    lock_b.acquire()
    print("Thread B has acquired lock B, calculating...")
    time.sleep(5)
    print("Thread B releasing both locks.")
    lock_b.release()
    lock_a.release()

lock_a = threading.Lock()
lock_b = threading.Lock()
thread_1 = threading.Thread(target = thread_a)
thread_2 = threading.Thread(target = thread_b)
start = timer()
thread_1.start()
thread_1.join()
thread_2.start()
thread_2.join()

print(f"Took {timer() - start:.2f} seconds.")
print("Done.")