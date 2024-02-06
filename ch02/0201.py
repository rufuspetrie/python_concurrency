from math import sqrt
import concurrent.futures
import multiprocessing
from timeit import default_timer as timer

def is_prime(x):
    if x < 2 or x == 2 or x % 2 == 0: return False
    lim = int(sqrt(x)) + 1
    for i in range(3, lim, 2):
        if x % i == 0: return False
    return x

def concurrent_solve(n_workers):
    print(f"Number of workers: {n_workers}")
    t0 = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers = n_workers) as executor:
        futures = [executor.submit(is_prime, i) for i in input]
        completed_futures = concurrent.futures.as_completed(futures)
        t00 = timer()
        for i, future in enumerate(completed_futures):
            if future.result(): result.append(future.result())
        sub_time = timer() - t00
    time = timer() - t0
    print(f"Subprocess took {sub_time:.4f} seconds")
    print(f"Total time: {time:.4f} seconds")

if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    input = [i for i in range(10**13, 10**13 + 1000)]
    for n_workers in range(1, multiprocessing.cpu_count() + 1):
        concurrent_solve(n_workers)
        print("_" * 20)