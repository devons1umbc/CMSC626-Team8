import time
import random
import argparse
from main import search, read, write_v2

NUM_REQUESTS = 100000

def random_read_benchmark():
    print("Random Read Benchmark:")
    for _ in range(NUM_REQUESTS):
        filename = f"random_file_{random.randint(1, 1000)}"
        start_time = time.time()
        result = read(filename)
        end_time = time.time()
        print(f"Read {filename}: {result}, Time: {end_time - start_time} seconds")

def random_write_benchmark():
    print("Random Write Benchmark:")
    for _ in range(NUM_REQUESTS):
        filename = f"random_file_{random.randint(1, 1000)}"
        message = f"Random content {random.randint(1, 100)}"
        start_time = time.time()
        result = write_v2(filename, message)
        end_time = time.time()
        print(f"Write {filename}: Result: {result}, Time: {end_time - start_time} seconds")

def main():
    parser = argparse.ArgumentParser(description="Benchmark script for testing read and write operations.")
    parser.add_argument("--read", action="store_true", help="Run random read benchmark.")
    parser.add_argument("--write", action="store_true", help="Run random write benchmark.")
    args = parser.parse_args()

    if args.read:
        random_read_benchmark()

    if args.write:
        random_write_benchmark()

if __name__ == "__main__":
    main()
