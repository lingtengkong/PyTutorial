import os
from concurrent.futures import ProcessPoolExecutor
from functools import reduce


def square(x):
    """Function to return the square of the argument"""
    print(f"Worker {os.getpid()} calculating square of {x}")
    return x * x


if __name__ == "__main__":
    # create a pool of workers
    with ProcessPoolExecutor(max_workers=5) as pool:
        # create an array of 20 integers, from 1 to 20
        r = range(1, 21)

        result = pool.map(square, r)

    # not be able to use lambda in the pool.map function.
    total = reduce(lambda x, y: x + y, result)

    print(f"The sum of the square of the first 20 integers is {total}")
