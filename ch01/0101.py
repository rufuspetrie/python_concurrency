from math import sqrt
import time
import concurrent.futures

def is_prime(x):
    if x < 2 or x == 2 or x % 2 == 0: return False
    lim = int(sqrt(x)) + 1
    for i in range(3, lim, 2):
        if x % i == 0: return False
    return x

# Note: need main protection for doing many paralell tasks
if __name__ == "__main__":
    
    # Example of sequential process
    input = [i for i in range(10**13, 10**13 + 500)]
    t0 = time.time()
    result = []
    for i in input:
        if is_prime(i): result.append(i)
    print(f"Result 1: {result}")
    print(f"Computation time: {time.time() - t0:.2f} seconds")

    # Example of parallel process
    t0 = time.time()
    result = []
    with concurrent.futures.ProcessPoolExecutor(max_workers = 20) as executor:
        futures = [executor.submit(is_prime, i) for i in input]
        for _, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                result.append(future.result())
    print(f"Result 2: {result}")
    print(f"Computation took {time.time() - t0:.2f} seconds")