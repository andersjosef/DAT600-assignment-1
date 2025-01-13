public class SortingAlgorithms {
    public static void insertion_sort(int[] n) {
        for (int j = 1; j < n.length; j++)
        {
            int key = n[j];
            int i = j -1;
            while (i >= 0 && n[i] > key)
            {
                n[i+1] = n[i];
                i--;
            }
            n[i +1] = key;
        }
        System.out.println("Im insertion sort!");
    }
    public static void heap_sort() {
        System.out.println("Im heap sort!");
    }
}

class Heap {
    int[] array;
    int heapSize;
    Heap(int[] array) {
        this.array = array;
        this.heapSize = array.length;
    }
}
