# Counting Sort Algorithm (Linear)
# Followed this for guidance: https://www.geeksforgeeks.org/counting-sort/

import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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


def countSort(arr):

    maxVal = max(arr)

    # 1. Frequency array for count of unique elements in input array   
    countArr = [0 for i in range(maxVal+1)]
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

def rgb_countSort(arr, color_component):

    #component_values = [value for tuple in arr for value in tuple]
    component_values = [rgb[color_component] for rgb in arr]
    maxVal = max(component_values)
    #print(maxVal)

    # 1. Frequency array for count of unique elements in input array   
    countArr = [0 for i in range(256)]
    for rgb in arr:
        countArr[rgb[color_component]] += 1

    # 2. Modify freq array to store running sum of its own elements
    for i in range(1, 256):
        countArr[i] += countArr[i - 1]
 
    # 3. Create output array (list) with len equal to # of elements
    outputArr = [0 for i in range(countArr[-1])]

    for rgb in reversed(arr):
        outputArr[countArr[rgb[color_component]] - 1] = rgb    # Place numbers in correct position in outputArr
        countArr[rgb[color_component]] -= 1                       # Decrement cumulative count after adding a number

    return outputArr

# Applies radixSort to pixels array, once for each color_component, starting with 2 (B/blue)
def radixSort(arr):

    for color_component in reversed(range(3)):
        pixels = rgb_countSort(arr, color_component) # 0 - Red, 1 - Green, 2 - Blue
        #print(pixels)
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

    n = 10 # Size of dataset/array (i.e., number of pixels)

    # Loop over n
    while n <= 10:

        #pixels = [(45, 25, 250), (223, 134, 70), (80, 90, 100), (20, 20, 20), (250, 250, 250), (38, 183, 29), (100, 100, 234)]
        #print(f"Unsorted array of pixels: {pixels}")

        # Create random data set & copy it
        data = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range (n)]
        data2 = list(data)

        # Display colors before
        display_colors(data)

        print(f"Unsorted lists:")
        print(f"Radix: {data}\nBubble: {data2}\n")
        # Time Count Sort (Radix Sort)
        t1 = time.perf_counter()
        data = radixSort(data)
        t1 = time.perf_counter() - t1

        print(f"Sorted: {data}")
        # Time Bubble Sort
        t2 = time.perf_counter()
        num_passes = bubbleSort(data2)
        t2 = time.perf_counter() - t2

        
        print(f"Sorted lists:")
        print(f"Radix: {data}\nBubble: {data2}\n")

        print(f"Size: {n}\nRadix Sort time: {t1:0.6f} sec\nBubble Sort time: {t2:0.6f} sec")

        # Display colors?
        #display_colors(data)
        # Double n each time
        n *= 2

    
if __name__ == "__main__":
    main()