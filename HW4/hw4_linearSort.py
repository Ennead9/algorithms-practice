# Counting Sort Algorithm (Linear)
# Followed this for guidance: https://www.geeksforgeeks.org/counting-sort/

import random
import time

def countSort(arr):
    maxVal = max(arr)
    countArr = [0 for i in range(maxVal+1)]

    # 1. Frequency array for count of unique elements in input array   
    for i in arr:
        countArr[i] += 1

    # 2. Modify freq array to store running sum of its own elements
    for i in range(1, len(countArr)):
        countArr[i] = countArr[i - 1] + countArr[i]
 
    # 3. Create output array (list) with len equal to # of elements
    outputArr = [0 for i in range(countArr[-1])]

    # Traverse input array from end to preserve stability
    # Value at countArr[arr[i]] represents cumulative count of the element arr[i] in original array
        # Cumulative count indicates total # of elements in original array that are less than or equal to arr[i]
        # -1 part is to adjust for zero-based indexing
        # EXAMPLE:
        # For arr[i] = 3 & countArr[i] =5, there are 5 elements in arr that are <= 3
        # To place 3 in sorted array, need to put it in the 4th position, so: countArr[3] - 1 = 4
    for i in range(len(arr) - 1, -1, -1):
        outputArr[countArr[arr[i]] - 1] = arr[i]    # Place numbers in correct position in outputArr
        countArr[arr[i]] -= 1                       # Decrement cumulative count after adding a number

    # Print sorted array
    #print(f"Sorted array: {outputArr}")

def main():

    n = 100000 # Size of array
    while n <= 600000:

        # Randomly populate data array with numbers between 0 & 1000
        data = [random.randint(0, 1000) for _ in range(n)]

        # Call quickSort function & time using perf_counter()
        t = time.perf_counter()
        countSort(data)
        t = time.perf_counter() - t

        print(f"\nTime (size: {n}): {t:.6f}\n")

        # Double n each time
        n *= 2

    
if __name__ == "__main__":
    main()