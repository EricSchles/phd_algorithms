from typing import List, Tuple
import numpy as np
import random

def max_crossing_subarray(arr: List, low: int, mid: int, high: int) -> Tuple:
    max_left = None
    max_right = None
    left_sum = -1 * np.inf
    summation = 0
    for i in range(mid, low-1, -1):
        summation += arr[i]
        if summation > left_sum:
            left_sum = summation
            max_left = i
    right_sum = -1 * np.inf
    summation = 0
    for i in range(mid+1, high+1):
        summation += arr[i]
        if summation > right_sum:
            right_sum = summation
            max_right = i
    if max_left is None:
        max_left = mid
    if max_right is None:
        max_right = mid+1
    return max_left, max_right, left_sum + right_sum
    
def max_subarray(arr: List, low: int, high: int)-> Tuple:
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,-10]
    low, high, summation = max_subarray(arr, 0, len(arr)-1)
    assert low == 0
    assert high == 5
    assert summation == sum(list(range(7)))

    random_left = [random.randint(1, 500) for _ in range(100)]
    random_right = [random.randint(1, 500) for _ in range(12)]
    left_sum = sum(random_left)
    right_sum = sum(random_right)

    arr = random_left + [-9999999999999999999999] + random_right
    low, high, summation = max_subarray(arr, 0, len(arr)-1)
    if left_sum > right_sum:
        assert low == 0
        assert high == 99
        assert summation == left_sum
    else:
        assert low == len(random_left)
        assert high == len(random_left) + len(random_right) -1
        assert summation == right_sum

    random_left = [random.randint(1, 10) for _ in range(100)]
    random_right = [random.randint(10000, 999999) for _ in range(12)]
    left_sum = sum(random_left)
    right_sum = sum(random_right)

    arr = random_left + [-999999999999999999999999] + random_right
    low, high, summation = max_subarray(arr, 0, len(arr)-1)
    if left_sum > right_sum:
        assert low == 0
        assert high == 98
        assert summation == left_sum
    else:        
        assert low == len(random_left)+1
        assert high == len(random_left) + len(random_right)
        assert summation == right_sum
