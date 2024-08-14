package amazon.q1;

import java.util.Arrays;

public class Solution {
    public int[] minimalHeaviestSetA(int arr[]) {
        int n = arr.length;
        quickSort(arr, 0, n - 1);

        int sum = calculateSum(arr, 0, n - 1);

        int minSumA = 0;
        int lowerLimit = n - 1;
        for (int j = n - 1; j >= 0; j--) {
            minSumA += arr[j];
            
            if(minSumA > sum - minSumA) {
                lowerLimit = j;
                break;
            }
        }
        return Arrays.copyOfRange(arr, lowerLimit, n-1);
    }

    public int calculateSum(int arr[], int low, int high) {
        int sum = 0;
        for (int i = low; i <= high; i++) sum += arr[i];
        return sum;

    }

    public void quickSort(int arr[], int low, int high) {
        int partition = partition(arr, low, high);
        quickSort(arr, low, partition - 1);
        quickSort(arr, partition + 1, high);
    }

    public int partition(int arr[], int low, int high) {
        int pivot = arr[high];

        int i = low - 1;
        for(int j = low; j <= high; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }


    public void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
