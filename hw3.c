#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *first, int *second){
    int temp = *first;
    *first = *second;
    *second = temp;
}
// Find pivot and sort array
int partition(int arr[], int lower, int upper){
    
    int pivot = arr[upper]; // Set pivot (n-1)
    int i = (lower - 1);
    int j;

    // Loop over array to compare against pivot val
    for(j = lower; j < upper; j++){
        if(arr[j] < pivot){
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[upper]); // Swap pivot so it's in the right spot

    return i;
}
// Recursive quickSort function
void quickSort(int arr[], int lower, int upper)
{
    int partitionIndex = partition(arr, lower, upper);

    if(upper > lower){
        
        int partitionIndex = partition(arr, lower, upper);

        quickSort(arr, lower, partitionIndex-1);
        quickSort(arr, partitionIndex + 1, upper);
    }
}

int main()
{
    clock_t t;

    // Create data set
    int data[7] = {3, 6, 7, 5, 1, 2, 4};

    printf("Before: ");
    for(int i = 0; i < 7; i++){
        printf("%d ", data[i]);
    }
    printf("\n");
    
    // Call quicksort, time using clock()
    t = clock();
    quickSort(data, 0, 6);
    t = clock() - t;
    double elapsed = ((double)t)/CLOCKS_PER_SEC;

    printf("\nSorted: ");
    for(int i = 0; i < 7; i++){
        printf("%d ", data[i]);
    }
    printf("\nTime: %f", elapsed);

    return 0;
}
