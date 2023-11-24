import random
import time
import sys # attempting to force it to handle 1.6m data set size :P

def quickSort(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        lower, upper = stack.pop()

        if upper >= lower:
            continue

        pivot = arr[upper]
        partition_index = lower
        for j in range(lower, upper):
            if arr[j] <= pivot:
                arr[j], arr[partition_index] = arr[partition_index], arr[j]
                partition_index += 1
        
        arr[partition_index], arr[upper] = arr[upper], arr[partition_index]

        if partition_index - 1 > lower:
            stack.append((lower, partition_index - 1))
        if partition_index + 1 > upper:
            stack.append((partition_index + 1, upper))

def main():
    
    n = 100000  # size of array
    while n <= 1000000:

        # randomly populate data array with numbers between 0 & 1000
        data = [random.randint(0, 1000) for _ in range(n)]

        # Call quickSort & time using perf_counter()
        t = time.perf_counter()
        quickSort(data)
        t = time.perf_counter() - t
    
        print(f"\nTime (size: {n}): {t:.6f}\n")

        n *= 2 # Double n each time

if __name__ == "__main__":
    main()