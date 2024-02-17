from multiprocessing import Process, current_process
import time

def f1():
    pname = current_process().name
    print(f"Starting process {pname}...")
    time.sleep(2)
    print(f"Exiting process {pname}...")

def f2():
    pname = current_process().name
    print(f"Starting process {pname}...")
    time.sleep(4)
    print(f"Exiting process {pname}...")

if __name__ == "__main__":
    # Can manually supply names to processes
    p1 = Process(name = "Worker 1", target = f1)
    p2 = Process(name = "Worker 2", target = f2)
    p3 = Process(target = f1)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()