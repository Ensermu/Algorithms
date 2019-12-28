def peak(A, s, e):
    mid = (s+e)//2
    if s == e:
        return A[s]
    else:
        if A[mid-1] > A[mid]:
            return peak(A, s, mid-1)
        elif A[mid+1] > A[mid]:
            return peak(A, mid+1, e)
        else:
            return A[mid]
