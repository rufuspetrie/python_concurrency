import concurrent.futures
from timeit import default_timer as timer

# Function to be run recursively
def f(x):
    return x**2 - x + 1

if __name__ == "__main__":
    
    # Sequential computation
    t0 =  timer()
    result = 3
    for i in range(20): result = f(result)
    print(f"Last 5 digits of result: {result % 10**4}")
    print(f"Sequential computation took: {timer() - t0} seconds")

    # Concurrent computation - note that concurrency does not help this process because 
        # the results are serially correlated
    def concurrent_f(x):
        global result
        result = f(result)
    t0 = timer()
    result = 3
    with concurrent.futures.ThreadPoolExecutor(max_workers = 20) as executor:
        futures = [executor.submit(concurrent_f, i) for i in range(20)]
        _ = concurrent.futures.as_completed(futures)
    print(f"Last 5 digits of result: {result % 10**4}")
    print(f"Sequential computation took: {timer() - t0} seconds")