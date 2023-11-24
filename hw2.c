#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *first, int *second){
    int temp = *first;
    *first = *second;
    *second = temp;
}
int partition(int arr[], int lower, int upper){
    
    int pivot = arr[upper]; // Set pivot (n-1)
    int i = (lower - 1);
    int j;

    // Loop over array to compare against pivot val
    for(j = lower; j < upper; j++){
        if(arr[j] < pivot){
            i++;
            swap();
        }
    }
}
void quickSort(int arr[], int low, int high)
{
    int partitionIndex = partition(arr, low, high);

    if(j < pivot){ // value at j is less than pivot

    }
}

int main()
{
    int size = 7;
    // Main loop (loop over n)
    for(int n = 0; n <= size; n++)
    {
        //int *data = (int *)malloc(n * sizeof(int));
        printf("--------- Start of loop %d ----------\n", n);

        // Static array for testing
        int data[7] = {4, 2, 7, 5, 1, 6, 3};
        /* Randomly construct data set of size n
        for(int i = 0; i < n; i++)
        {
            data[i] = rand() % 1001;
        }*/

        // Call function on data set
        //quickSort(data, 0, n - 1);

        // Print result
        for(int i = 0; i < size; i++)
        {
            printf("Val: %d at data[%d]\n", data[i], i);
        }
        printf("----- End of loop %d-------\n", n);
    }

    return 0;
}
