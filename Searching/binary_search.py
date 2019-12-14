def Binary_Search(A, s, n, v):
    mid = (s + n) // 2
    if v == A[mid]:
        print('index =', mid)
        return A[mid]
    if s == mid:
        return
    if v < A[mid]:
        return Binary_Search(A, s, mid, v)
    else:
        return Binary_Search(A, mid+1, n, v)
