def HEAP_SORT(unsorted_list):					
    sorted_list = []
    max_heap = Build_Max_Heap(unsorted_list)
    while len(max_heap)!= 0:
        last_element = len(max_heap) - 1
        key = max_heap[0]							
        max_heap[0] = max_heap[last_element]					
        max_heap[last_element] = key			
        sorted_list.append(max_heap[last_element])
        max_heap.pop()	
        Max_Heapify(max_heap, 0)        					   
    sorted_list.reverse()
    return sorted_list

def Build_Max_Heap(heap):						
    j = (len(heap) // 2) - 1
    for j in range(j, -1, -1):	
        Max_Heapify(heap, j)
    return heap
    
def Max_Heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
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
