import threading
from math import sqrt

def is_prime(x):
    if x == 2: print(f"{x} is a prime number")
    elif x < 2  or x % 2 == 0: print(f"{x} is not a prime number")
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print(f"{x} is not a prime number")
                return
        print(f"{x} is a prime number")

# Unlike the _thread module, which can simply make a function a thread,
    # the threading module makes each thread into a class object
class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        print(f"Processing {x}...")
        is_prime(self.x)

# thread.join() ensures that each thread finishes before the program terminates
my_input = [2, 193, 323, 1327, 433785907]
threads = []
for x in my_input:
    temp_thread = MyThread(x)
    temp_thread.start()
    threads.append(temp_thread)
for thread in threads: 
    thread.join()
print("Finished")