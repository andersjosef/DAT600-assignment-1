# Insertion sort


def insertion_sort(n):
    for j in range(1, len(n)):
        key = n[j]
        i = j - 1
        while i >= 0 and n[i] > key:
            n[i+1] = n[i]
            i = i - 1
        n[i + 1]  = key


# # Merge Sort
# def merge(A, p, q, r):

#     left = A[p:q+1]
#     right = A[q+1:r+1]

#     i = 0
#     j = 0
#     k = p

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             A[k] = left[i]
#             i += 1
#         else:
#             A[k] = right[j]
#             j += 1
#         k += 1
    
#     while i < len(left):
#         A[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         A[k] = right[j]
#         j += 1
#         k += 1


# def merge_sort_internal(A, p, r):
#     if p >= r: # Zero or one element
#         return
#     q = (p + r)//2
#     merge_sort_internal(A, p, q) # Left 
#     merge_sort_internal(A, q+1, r) # Right
#     merge(A, p, q, r)

# # Simpler calling without having to specify the range when calling
# def merge_sort(array):
#     merge_sort_internal(array, 0, len(array))


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


# # Quick Sort

# def partition(A, p, r):
#     x = A[r]
#     i = p - 1

#     for j in range(p, r):
#         if A[j] <= x:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#     A[i+1], A[r] = A[r], A[i+1]
#     return i + 1


# def quick_sort_internal(A, p, r):
#     if p < r:
#         q = partition(A, p, r)
#         quick_sort_internal(A, p, q-1) # recursive low side
#         quick_sort_internal(A, q+1, r) # recursive high side

# # For easier usage
# def quick_sort(array):
#     quick_sort_internal(array, 0, len(array)-1)
