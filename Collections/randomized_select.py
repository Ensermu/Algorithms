import random

def Randomized_Select(A, p, r, i):
	if p == r:
		return A[p]
	q = Randomized_Partition(A, p, r)
	k = q - p + 1
	if i == k:
		return A[q]
	elif i < k:
		return Randomized_Select(A, p, q - 1, i)
	else:
		return Randomized_Select(A, q + 1, r, i - k)

def Randomized_Partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return Partition(A, p, r)

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1