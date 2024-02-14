import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Starting thread {self.name}")
        process_queue()
        print("Exiting thread {self.name}")

def process_queue():
    while True:
        try:
            x = my_queue.get(block = False)
        except queue.Empty:
            return
        else:
            print_factors(x)
        time.sleep(1)

def print_factors(x):
    result_string = f"Positive factors of {x} are: "
    for i in range(1, x + 1):
        if x % i == 0: result_string += str(i) + " "
    result_string += "\n" + "_" * 20
    print(result_string)

input_ = [1, 10, 4, 3]
my_queue = queue.Queue()
for x in input_: my_queue.put(x)

thread_1 = MyThread("A")
thread_2 = MyThread("B")
thread_3 = MyThread("C")

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Finished")