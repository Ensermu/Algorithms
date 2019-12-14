def priority_queue_sort(A):
	Q = []
	for x in A:
		insert(Q, x)
	for i in range(len(A)):
		A[len(A)-1-i]=delete_max(Q)
	return A

def insert(Q, x):
	Q.append(x)

def delete_max(Q):
	best = 0
	for i in range(len(Q)):
		if Q[i] > Q[best]:
			best=i
	Q[i], Q[best] = Q[best], Q[i]
	return Q.pop()
