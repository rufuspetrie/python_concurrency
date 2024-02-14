import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting thread {self.name}")
        thread_lock.acquire()
        thread_count_down(self.name, self.delay)
        thread_lock.release()
        print(f"Finished thread {self.name}")

def thread_count_down(name, delay):
    counter = 5
    while counter:
        time.sleep(delay)
        print(f"Thread {name} counting down: {counter}")
        counter -= 1

# Notice that although we implement the countdown using separate threads,
    # they count down separately because we use a thread lock
thread_lock = threading.Lock()
thread_1 = MyThread("A", 0.5)
thread_2 = MyThread("B", 0.5)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("Finished")