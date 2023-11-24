import random
import time

def partition(arr, lower, upper):
    pivot = arr[upper]
    i = (lower - 1)

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
        quickSort(arr, partition_index+1, upper)


def main():
    
    n = 10  # size of array
    test = [random.randint(0, 1000) for _ in range(n)] # randomly populate test array with numbers between 0 & 1000
    print("Before: ")
    # print array contents
    for i in test:
        print(i, end=' ')

    t = time.perf_counter()
    quickSort(test, 0, n-1)
    t = time.perf_counter() - t
    
    print("After: ")
    for i in test:
        print(i, end=' ')
    print(f"Time elapsed: {t:.6f}")

if __name__ == "__main__":
    main()