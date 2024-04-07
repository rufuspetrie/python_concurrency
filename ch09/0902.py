from math import sqrt
import asyncio

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
            elif i % 100000 == 1:
                await asyncio.sleep(0)
        print(f"{x} is a prime number.")

async def main():
    task1 = loop.create_task(is_prime(9637529763296797))
    task2 = loop.create_task(is_prime(427920331))
    task3 = loop.create_task(is_prime(157))
    await asyncio.wait([task1, task2, task3])

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print("There was a problem: ")
        print(str(e))
    finally:
        loop.close()