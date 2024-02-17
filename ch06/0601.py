from multiprocessing import Process
import time

def count_down(name, delay):
    print(f"Process {name} starting...")
    counter = 5
    while counter:
        time.sleep(delay)
        print(f"Process {name} counting down: {counter}...")
        counter -= 1
    print(f"Process {name} exiting")

if __name__ == "__main__":
    p1 = Process(target = count_down, args = ("A", 0.5))
    p2 = Process(target = count_down, args = ("B", 0.5))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Finished")