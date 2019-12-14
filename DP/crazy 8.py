memo = {}
parent = {}
def Crazy_Eight(L):
    '''the longest same number sequence'''
    result = 1
    for i in range(len(L)-1, -1, -1):
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                memo[i] = 1 + memo[j]
                parent[j] = i
                break
        if i not in memo:
            memo[i] = result
    return max(memo.values())
