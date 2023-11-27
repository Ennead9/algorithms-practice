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

    return outputArr

def bubbleSort(arr):
    num_passes = 0

    # Outer loop to move onto next number to move/sort
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        num_passes += 1
        if not swapped:
            break
    return num_passes


def greyscaleValue(pixel):
    return int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


def main():

    n = 10 # Size of dataset/array (i.e., number of pixels)

    # Loop over n
    while n <= 40:

        # Randomly populate data array with RGB values
        pixels_list = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(n)]

        greyscale_list = [greyscaleValue(pixel) for pixel in pixels_list]
        #print(greyscale_list)

        data2 = list(greyscale_list)  # Copy list

        # Call linear (countSort) function & time using perf_counter()
        t1 = time.perf_counter()
        data = countSort(greyscale_list)
        t1 = time.perf_counter() - t1

        # Call comparison (bubbleSort) function & time
        t2 = time.perf_counter()
        num_passes = bubbleSort(data2)
        t2 = time.perf_counter() - t2

        # Print results
        print(f"\nSize: {n}\nCount Sort time: {t1:.6f}\nBubble Sort time: {t2:.6f}\nSorted in {num_passes} passes")

        # Double n each time
        n *= 2

    
if __name__ == "__main__":
    main()