# Insertion sort

def insertion_sort(n):
    for j in range(1, len(n)):
        key = n[j]
        i = j - 1
        while i >= 0 and n[i] > key:
            n[i+1] = n[i]
            i = i - 1
        n[i + 1]  = key

# Heap sort

class Heap:
    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)

def left(i):
    return i*2+1

def right(i):
    return i*2+2

def parent(i):
    return i//2


def max_heapify(A:Heap, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A.array[l] > A.array[i]:
        largest = l
    else:
        largest = i
    
    if r <= A.heap_size and A.array[r] > A.array[largest]:
        largest = r
    
    if largest != i:
        A.array[i], A.array[largest] = A.array[largest], A.array[i]
        max_heapify(A, largest)

def build_max_heap(A:Heap, n):
    A.heap_size = n
    for i in range(n//2, -1, -1): # Down to and including 0
        max_heapify(A, i)

def heap_sort_internal(A:Heap, n):
    build_max_heap(A, n)
    for i in range(n, 0, -1): # Step range go backwards from n-1 to but not including 0
        A.array[0], A.array[i] = A.array[i], A.array[0] # Change first index with i
        A.heap_size -= 1
        max_heapify(A, 0)

def heap_sort(array):
    heap = Heap(array=array)
    heap_sort_internal(heap, len(heap.array)-1)
