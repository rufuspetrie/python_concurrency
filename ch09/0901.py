from math import sqrt

def is_prime(x):
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
        print(f"{x} is a prime number.")

if __name__ == "__main__":
    is_prime(9637529763296797)
    is_prime(427920331)
    is_prime(157)