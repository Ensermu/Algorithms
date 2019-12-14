options = []
n = len(c)
def summ(a, b, c):
    return a + b + c

def cmp(a, b):
    return(a > b) - (a < b)
    
def BJ(i):
    if n - i < 4: return 0
    for p in range(2, n - i - 2):
        player = summ(c[i], c[i+2], sum(c[i+4:i+p+2]))
        if player > 21:
            options.append(-1 + BJ(i+p+2))
            break
        for d in range(2, n-i-p):
            dealer = summ(c[i+1], c[i+3], sum(c[i+p+2:i+p+d]))
            if dealer >= 17: break
        if dealer > 21: dealer = 0
        options.append(cmp(player, dealer) + BJ(i+p+d))
    return max(options)
