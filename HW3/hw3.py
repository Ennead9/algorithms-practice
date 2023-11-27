# Quick Sort Algorithm
# Adapted from C implementation on "The Algorithms" page on GitHub
# Found here: https://github.com/TheAlgorithms

import random
import time

# Find pivot & sort array
def partition(arr, lower, upper):
    pivot = arr[upper]
    i = (lower - 1)

    # Loop over array to compare against pivot
    for j in range(lower, upper):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[upper] = arr[upper], arr[i + 1]
    return i + 1

def quickSort(arr, lower, upper):
    if upper > lower:
        partition_index = partition(arr, lower, upper)

        quickSort(arr, lower, partition_index-1)
        quickSort(arr, partition_index + 1, upper)


def main():

    # Size of array
    n = 100000
    while n <= 600000:

        # Randomly populate data array with numbers between 0 & 1000
        data = [random.randint(0, 1000) for _ in range(n)]

        # Call quickSort & time using perf_counter()
        t = time.perf_counter()
        quickSort(data, 0, n-1)
        t = time.perf_counter() - t
    
        print(f"\nTime (size: {n}): {t:.6f}\n")

        # Double n each time
        n *= 2

if __name__ == "__main__":
    main()