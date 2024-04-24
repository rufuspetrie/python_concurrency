import threading

def philosopher(left, right):
    while True:
        with left:
            with right:
                print(f"Philosopher at {threading.currentThread()} is eating.")

n_forks = 5
forks = [threading.Lock() for n in range(n_forks)]

phils = [threading.Thread(
    target = philosopher,
    args = (forks[n], forks[(n + 1) % n_forks])
) for n in range(n_forks)]

for p in phils:
    p.start()