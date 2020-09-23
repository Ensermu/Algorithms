import math
coordinates = [(1, 1), (-2, 4), (-1, 2), (2, 3), (3, 5), (-3, 6), (0, 8), (.45, 7.5), (-1.1, 1.9)]
X = sorted(coordinates)
Y = sorted(coordinates, key = lambda x:x[1])

def Closest_Points(points, Y):
    if len(points) <= 3:
        return brute_force(points)
    middle = X[math.ceil(len(points) / 2) - 1]
    P = []
    Q = []
    YL = []
    YR = []
    for i in range(len(points)//2):
        P.append(points[i])
    for i in range(len(points)//2, len(points)):
        Q.append(points[i])
    for i in Y:
        if i in P:
            YL.append(i)
        else:
            YR.append(i)
    delta1 = Closest_Points(P, YL)
    delta2 = Closest_Points(Q, YR)
    delta = min(delta1, delta2)
    S = []
    S.append(middle)
    for i in Y:
        if i != middle and abs(dist(middle, i)) <= delta:
            S.append(i)
    for i in range(len(S)):
        for j in range(i+1, i+9):
            if j < len(S):
                distance = dist(S[i], S[j])
                if distance < delta:
                    delta = distance
    return delta

def dist(p1, p2):
    return pow(pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2), 1/2)
     
def brute_force(points):
    closest = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            distance = dist(points[i], points[j])
            if distance < closest:
                closest = distance
    return closest  
     
print(Closest_Points(X, Y))
