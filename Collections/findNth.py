import math
def findNth(a, b):
    i = math.floor((a+b)/2)
    j = n - i - 1
    if l1[i] < l2[j]:
        if l1[i+1] > l2[j]:
            return l2[j]
        else:
            return findNth(i+1, b)
    else:
        if l2[j+1] > l1[i]:
            return l1[i]
        else:
            return findNth(a, i-1)
