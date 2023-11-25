# Linear Sort Algorithm
# Sorting pixels based on color values?

def countSort(arr):
    maxVal = max(arr)
    digits = len(str(maxVal))
    print(f"Digits: {digits} maxVal: {maxVal}")

    outputArr = [0 for i in range(maxVal+1)]
    countArr = [0 for i in range(maxVal+1)]
    
    for i in arr:
        countArr[i] += 1
    for i in arr:
        countArr[i] = countArr[i - 1] + countArr[i]
    
    for i in reversed(arr):
        print(i)
        print(arr[i])
        outputArr[countArr[arr[i]]-1] = arr[i]

def main():

    # Create static list of RGB values
    
    # Create test list & print
    # data = [170, 45, 75, 90, 802, 24, 2, 66]
    data = [0, 3, 4, 6, 3, 2, 11]
    print(f"Unsorted: {data}\n")
    countSort(data)

if __name__ == "__main__":
    main()