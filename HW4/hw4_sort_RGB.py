# Counting Sort Algorithm (Linear)
# Followed this for guidance on counting sort: https://www.geeksforgeeks.org/counting-sort/
# Radix & Bubble were my own

import random
import time

# Original Counting Sort implementation
def countSort(arr):
    
    # Find maximum value to define range for countArr
    maxVal = max(arr)

    # 1. Initialize frequency array for count of unique elements in input array   
    countArr = [0 for i in range(maxVal+1)]
    for i in arr:
        countArr[i] += 1

    # 2. Modify frequency array to store running sum of its own elements
    for i in range(1, len(countArr)):
        countArr[i] = countArr[i - 1] + countArr[i]
 
    # 3. Initialize output array for sorted elements, with length equal to # of elements
    outputArr = [0 for i in range(countArr[-1])]
    
    # Traverse input array from end to start to maintain stability
    for i in range(len(arr) - 1, -1, -1):
        # Value at countArr[arr[i]] is the cumulative count of arr[i] in original array
        # This count determines position of arr[i] in the sorted output array
        # Subtract 1 to account for zero-based indexing
        # Example: For arr[i] = 3 and countArr[i] = 5, there are 5 elements <= 3
        # So, place 3rd element in the 4th position
        outputArr[countArr[arr[i]] - 1] = arr[i]    # Place numbers in correct position in outputArr
        countArr[arr[i]] -= 1                       # Decrement cumulative count after adding a number

    return outputArr


# Adjusted Counting Sort implementation for RGB tuples
def rgb_countSort(arr, color_component):

    # 1. Frequency array for count of unique elements in input array   
    countArr = [0 for i in range(256)]
    for rgb in arr:
        countArr[rgb[color_component]] += 1

    # 2. Modify freq array to store running sum of its own elements
    for i in range(1, 256):
        countArr[i] += countArr[i - 1]
 
    # 3. Create output array with length equal to number of elements
    outputArr = [0 for i in range(countArr[-1])]

    # Place values in correct position in output array
    for rgb in reversed(arr):
        outputArr[countArr[rgb[color_component]] - 1] = rgb
        countArr[rgb[color_component]] -= 1      # Decrement cumulative count after adding a number

    return outputArr


# Applies Radix Sort to RGB tuples array/list, sorting B -> G -> R
# R/G/B denoted by 0/1/2, respectively
def radixSort(arr):

    for color_component in reversed(range(3)):
        sortedArr = rgb_countSort(arr, color_component)
    return sortedArr


# Bubble Sort implementation
def bubbleSort(arr):
    num_passes = 0

    # Outer loop to move onto next number to move/sort
    for i in range(len(arr)):
        swapped = False
        # Inner loop to compare current value to others and swap accordingly
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        num_passes += 1
        if not swapped:
            break

    return arr

    
def main():

    n = 10  # Data set size
    print("n        Linear - Radix (ms)  Comparison - Bubble (ms)")

    # Loop over n, increasing by factor of 10 each time
    while n <= 10000:

        # Create random data set & copy it
        data = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range (n)]
        data2 = list(data)

        # Time Count Sort (Radix Sort)
        t1 = time.perf_counter()
        data = radixSort(data)
        t1 = (time.perf_counter() - t1) * 1000

        # Time Bubble Sort
        t2 = time.perf_counter()
        data2 = bubbleSort(data2)
        t2 = (time.perf_counter() - t2) * 1000

        # Print results
        print(f"{n:<6} {t1:>15.6f} {t2:>20.6f}")

        n *= 10

    
if __name__ == "__main__":
    main()