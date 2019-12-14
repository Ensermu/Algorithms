def Build_Max_Heap(heap):						
    j = len(heap) // 2
    for j in range(j, -1, -1):	
        Max_Heapify(heap, j)
    return heap

def Max_Heapify(A, i):
    left = 2*i + 1
    right = 2*i + 2
    if left < len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right < len(A) and A[right] > A[i] and A[right] > A[largest]:
        largest = right
    if largest != i:
        key = A[i]
        A[i] = A[largest]
        A[largest] = key
        Max_Heapify(A, largest)
    return A

def Heap_Maximum(A):
    return A[0]
    
def Heap_Extract_Max(A):
    if len(A) < 1:
        return 'error "heap underflow" '
    maximum = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    Max_Heapify(A, 0)
    return maximum

def Heap_Increase_Key(A, i, key):
    if key < A[i]:
        return 'error "new key is smaller than current key" '
    A[i] = key
    while i > 0 and A[i//2] < A[i]:
        A[i] = A[i//2]
        A[i//2] = key
        i = i//2
    return A[i]

def Max_Heap_Insert(A,key):
    A.append(key)
    Heap_Increase_Key(A,len(A)-1,key)
