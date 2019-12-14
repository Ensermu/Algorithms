def peak(A):
   if len(A) == 1:
       return A[0]
   if len(A) == 2:
        if A[0] >= A[1]:
            return A[0]
        else:
            return A[1]
   else:
    if A[int(len(A)/2)] >= A[int(len(A)/2)+1] and A[int(len(A)/2)] >= A[int(len(A)/2)-1]:
        return A[int(len(A)/2)]
    elif A[int(len(A)/2)] < A[int(len(A)/2)-1]:
        if len(A) == 3:
            return peak(A[0:int(len(A)/2)+1])
        else:
            return peak(A[0:int(len(A)/2)])
    else:
        if len(A) == 3:
            return peak(A[int(len(A)/2):len(A)])
        else:   
            return peak(A[int(len(A)/2)+1:len(A)])

