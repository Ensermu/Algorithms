def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = float('-inf')
    summ = 0
    max_left = mid
    max_right = mid
    for i in range(mid, -1, -1):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    right_sum = float('-inf')
    summ = 0
    for j in range(mid+1, high+1, 1):
        summ = summ + A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def FIND_MAXIMUM_SUBARRAY(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low+high) // 2
        (left_low,left_high,left_sum) = FIND_MAXIMUM_SUBARRAY(A, low, mid)
        (right_low,right_high,right_sum) = FIND_MAXIMUM_SUBARRAY(A, mid+1, high)
        (cross_low,cross_high,cross_sum) = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
