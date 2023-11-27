# Linear Sort Algorithm
# Sorting pixels based on color values?

def countSort(arr):
    maxVal = max(arr)
    digits = len(str(maxVal))
    print(f"Digits: {digits} maxVal: {maxVal}")

    countArr = [0 for i in range(maxVal+1)]
    
    # Count of unique elements in countArr
    for i in arr:
        countArr[i] += 1
    
    print(f"countArr: {countArr}")
    print("-----------")
    # Modify freq. array to store running sum of its own elements
    for i in range(1, len(countArr)):
        countArr[i] = countArr[i - 1] + countArr[i]
    
    print(f"countArr: {countArr}")

    # Create output array (list) with length equal to "# of elements"
    outputArr = [0 for i in range(countArr[-1])]
    print(outputArr)

    # Put stuff into output array
    # Put 
    for i in range(1, len(arr)):
        print(countArr[i])
    

def main():

    # Create static list of RGB values
    
    # Create test list & print
    # data = [170, 45, 75, 90, 802, 24, 2, 66]
    data = [0, 3, 4, 6, 3, 2, 7]
    print(f"Unsorted: {data}\n")
    countSort(data)

if __name__ == "__main__":
    main()