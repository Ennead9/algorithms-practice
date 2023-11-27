# Linear Sort Algorithm

def countSort(arr):
    maxVal = max(arr)
    digits = len(str(maxVal))
    #print(f"Digits: {digits} maxVal: {maxVal}")
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
    for i in range(len(arr) - 1, -1, -1):

        # Value at countArr[arr[i]] represents cumulative count of the element arr[i] in original array
        # Cumulative count indicates total # of elements in original array that are less than or equal to arr[i]
        # -1 part is to adjust for zero-based indexing
        # EXAMPLE:
        # If arr[i] is 3, and countArr[i] is 5, this means there are 5 elements in arr that are <= 3
        # To place 3 in sorted array, need to put it in the 4th position, so: countArr[3] - 1 = 4
        outputArr[countArr[arr[i]] - 1] = arr[i]
        countArr[arr[i]] -= 1 # need to decrement the cumulative count since we've already placed a number

    # Print sorted array
    print(f"Sorted array: {outputArr}")

def main():

    # Create test list & print
    data = [1, 0, 3, 4, 6, 3, 2, 7]
    print(f"Unsorted: {data}\n")
    countSort(data)

    
if __name__ == "__main__":
    main()