#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int quickSort(int arr[], int n)
{
    // Select pivot (any, but here is first val)
    int pivot = arr[n-1];
}

int main()
{
    // FILE type, create file pointer (*pF), open( file name, w for write);
    FILE *pF = fopen("logC.txt", "w");
    
    clock_t start, end;
    int times[3] = {0}; // Array to store 
    
    srand(time(NULL));
    
    // Loop over n
    for(int n = 50; n <= 200; n *= 2)
    {
        int arr[n];
        fprintf(pF, "Size: %d\n", n);
        
        
        
        // Create data set
        for(int i = 0; i < n; i++)
        {
            arr[i] = rand();
            fprintf(pF, "%d\n", arr[i]);
        }
        // Call function
        
        
        
        
        fprintf(pF, "End of set\n\n");
    }
    
    // Write results to file/log
    
    /* Test print
    for(int i = 0; i < n; i++)
    {
        printf("Val: %d\n", arr[i]);
    }*/
    
    fclose(pF); // Close file when done
    
    return 0;
}
