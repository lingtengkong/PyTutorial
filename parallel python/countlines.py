# import urllib.request
# import tarfile

# urllib.request.urlretrieve(
#     "https://milliams.com/courses/parallel_python/shakespeare.tar.bz2", "shakespeare.tar.bz2")
# with tarfile.open("shakespeare.tar.bz2") as tar:
#     tar.extractall()

from concurrent.futures import ProcessPoolExecutor
import glob
import sys
from functools import reduce


def count_lines_in_file(filename):

    with open(filename) as f:
        return len(f.readlines())


filenames = sorted(glob.glob(f"{sys.argv[1]}/*"))

play_line_count = list(map(count_lines_in_file, filenames))

print(list(zip(filenames, play_line_count)))

# total number


def add(x, y):
    return x + y


if __name__ == "__main__":
    # create a pool of workers

    filenames = sorted(glob.glob(f"{sys.argv[1]}/*"))

    with ProcessPoolExecutor(max_workers=5) as pool:
        play_line_count = list(pool.map(count_lines_in_file, filenames))

    print(list(zip(filenames, play_line_count)))

    total = reduce(add, play_line_count)

    print(f"total numbber is {total}")
