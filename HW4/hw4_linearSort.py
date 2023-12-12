# Counting Sort Algorithm (Linear)
# Followed this for guidance: https://www.geeksforgeeks.org/counting-sort/

import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    return num_passes

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
        pixels = rgb_countSort(arr, color_component)
        display_colors(pixels)
    return pixels


def display_colors(rgb_list, figsize=(10, 2)):
    fig, ax = plt.subplots(1, figsize=figsize)

    ax.axis('off')

    for i, rgb in enumerate(rgb_list):
        rect = patches.Rectangle((i, 0), 1, 1, linewidth=1, edgecolor='none', facecolor=[c/255 for c in rgb])
        ax.add_patch(rect)

    plt.xlim(0, len(rgb_list))
    plt.ylim(0, 1)

    plt.show()

    
def main():

    # Data set size
    n = 10

    # Loop over n, doubling n each time
    while n <= 10:

        # Create random data set & copy it
        data = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range (n)]
        data2 = list(data)

        # Display unsorted colors
        display_colors(data)

        # Debug: Print unsorted arrays
        #print(f"Unsorted:")
        #print(f"Radix: {data}\nBubble: {data2}\n")

        # Time Count Sort (Radix Sort)
        t1 = time.perf_counter()
        data = radixSort(data)
        t1 = time.perf_counter() - t1

        # Time Bubble Sort
        t2 = time.perf_counter()
        num_passes = bubbleSort(data2)
        t2 = time.perf_counter() - t2

        # Debug: Print sorted arrays
        #print(f"Sorted:")
        #print(f"Radix: {data}\nBubble: {data2}\n")

        print(f"Size: {n}\nRadix Sort time: {t1:0.6f} sec\nBubble Sort time: {t2:0.6f} sec")

        # Display sorted colors
        #display_colors(data)

        n *= 2

    
if __name__ == "__main__":
    main()