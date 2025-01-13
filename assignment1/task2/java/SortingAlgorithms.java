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
    }
    // The one called by the end user
    public static void heap_sort(int[] array) {
        Heap heap = new Heap(array);
        heap_sort_internal(heap, heap.array.length-1);
    }

    private static void heap_sort_internal(Heap A, int n)
    {
        build_max_heap(A, n);
        for (int i = n; i>=1; i--)
        {
            swap(A.array, 0, i);
            A.heapSize--;
            max_heapify(A, 0);
        }

    }
    
    private static void build_max_heap(Heap A, int n)
    {
        A.heapSize = n;
        for (int i = n/2; i>=0; i--)
        {
            max_heapify(A, i);
        }
    }

    private static void max_heapify(Heap A, int i)
    {
        int l = left(i);
        int r = right(i);
        int largest;
        if (l <= A.heapSize && A.array[l] > A.array[i])
        {
            largest = l;
        }
        else
        {
            largest = i;
        }
        if (r <= A.heapSize && A.array[r] > A.array[largest])
        {
            largest = r;
        }

        if (largest != i)
        {
            swap(A.array, i, largest);
            max_heapify(A, largest);
        }
    }

    // Helper function for swapping two elements in an array
    private static void swap(int[] array, int i1, int i2)
    {
        int tmp = array[i1];
        array[i1] = array[i2];
        array[i2] = tmp;
    }

    static int left(int i)
    {
        return i*2+1;
    }
    static int right(int i)
    {
        return i*2+2;
    }
    static int partent(int i)
    {
        return i/2;
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
