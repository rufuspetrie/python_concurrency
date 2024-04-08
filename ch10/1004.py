from math import sqrt
import asyncio
from timeit import default_timer as timer

async def is_prime(x):
    print(f"Processing {x}")
    if x < 2: print(f"{x} is not a prime number.")
    elif x == 2: print(f"{x} is a prime number.")
    elif x % 2 == 0: print(f"{x} is not a prime number.")
    else:
        lim = int(sqrt(x)) + 1
        for i in range(3, lim, 2):
            if x % i == 0:
                print(f"{x} is not a prime number.")
                return
            # Putting a sleep here allows us to switch to other coroutines
                # while performing large computations
            elif i % 100000 == 1:
                await asyncio.sleep(0)
        print(f"{x} is a prime number.")

async def main():
    task1 = loop.create_task(is_prime(9637529763296797))
    task2 = loop.create_task(is_prime(427920331))
    task3 = loop.create_task(is_prime(157))
    await asyncio.wait([task1, task2, task3])

# Note
    # The asynchronous version of this program takes longer because it mainly
        # consists of number crunching
    # Simply switching between different computations does not speed them up,
        # and we gain significant overhead from the asynchronous code
    # Therefore, we likely need to multithread/multiprocess to speed this up
if __name__ == "__main__":
    try:
        start = timer()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        print(f"Took {timer() - start:.4f} seconds")
    except Exception as e:
        print("There was a problem: ")
        print(str(e))
    finally:
        loop.close()