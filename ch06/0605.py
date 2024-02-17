from multiprocessing import Process, current_process
import time

def f1():
    p = current_process()
    print(f"Starting process {p.name}, ID {p.pid}")
    time.sleep(4)
    print(f"Exiting process {p.name}, ID {p.pid}")

def f2():
    p = current_process()
    print(f"Starting process {p.name}, ID {p.pid}")
    time.sleep(2)
    print(f"Exiting process {p.name}, ID {p.pid}")

if __name__ == "__main__":
    p1 = Process(name = "Worker 1", target = f1)
    p1.daemon = True
    p2 = Process(name = "Worker 2", target = f2)
    
    p1.start()
    time.sleep(1)
    p2.start()
    
    p1.join()
    print("Whether worker 1 is still going: ", p1.is_alive())
    p2.join()