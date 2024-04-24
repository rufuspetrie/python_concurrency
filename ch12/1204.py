import threading

class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key = lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False
    
def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(f"Philosopher at {threading.currentThread()} is eating.")

n_forks = 5
forks = [threading.Lock() for n in range(n_forks)]

phils = [threading.Thread(
    target = philosopher,
    args = (forks[n], forks[(n + 1) % n_forks])
) for n in range(n_forks)]

for p in phils:
    p.start()