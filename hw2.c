#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void quickSort(int arr[], int low, int high)
{
    int pivot = arr[high]; // Set n - 1 as pivot
    int i = low - 1;
    
    if(low < pivot){

    }
}

int main()
{

    clock_t start, end;
    double cpu_time_used;

    // Main loop (loop over n)
    for(int n = 50; n <= 200; n *= 2)
    {
        //int *data = (int *)malloc(n * sizeof(int));

        // Static array for testing
        int data[7] = {4, 2, 7, 5, 1, 6, 3};
        /* Randomly construct data set of size n
        for(int i = 0; i < n; i++)
        {
            data[i] = rand() % 1001;
        }*/

        // Call function on data set
        start = clock();
        quickSort(data, 0, n - 1);
        end = clock();

        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Size: %d, Time: %f\n", n, cpu_time_used);

        // Print result
        for(int i = 0; i < n; i++)
        {
            printf("Val: %d\n", data[i]);
        }

    }

    return 0;
}
