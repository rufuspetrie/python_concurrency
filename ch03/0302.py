# Note that _thread is the python 2.x version
import _thread as thread
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

# Notice that the program does not always output the results in this order
my_input = [2, 193, 323, 1327, 433785907]
for x in my_input:
    thread.start_new_thread(is_prime, (x, ))

# Without asking for input, the program will terminate before the threads finish running
# The more modern threading module doesn't really have this problem
a = input("Type something to quit: \n")
print("Finished")