# Notice that because each process is assigned its own thread,
    # the two processes count down at the same time
from my_thread import MyThread

thread_1 = MyThread("A", 0.5)
thread_2 = MyThread("B", 0.5)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("Finished.")