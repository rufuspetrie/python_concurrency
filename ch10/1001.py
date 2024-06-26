import time

def count_down(name, delay):
    indents = (ord(name) - ord("A")) * "\t"
    n = 3
    while n:
        time.sleep(delay)
        duration = time.perf_counter() - start
        print ("-" * 40)
        print(f"{duration:.4f} \t {indents}{name} = {n}")
        n -= 1

start = time.perf_counter()
count_down("A", 1)
count_down("B", 0.8)
count_down("C", 0.5)
print("-" * 40)
print("Done.")