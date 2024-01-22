import pytest
from typing import List

def countIncresaingMasking(arr: List[int]) -> int:

    def forwardTable(arr):
        res = [0]*len(arr)
        res[0] = 1
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                break
            res[i] = 1
        return res

    def backwardTable(arr):
        n = len(arr)
        res = [0]*n
        res[n-1] = 1
        for i in range(1, n):
            if arr[n-i-1] >= arr[n-i]:
                break
            res[n-i-1] = 1
        return res

    res = 0
    forward = forwardTable(arr)
    backward = backwardTable(arr)
    if forward[-1] == 1:
        res += 1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i-1 == -1 and j+1 == len(arr):
                res += 1
            elif i-1 == -1 and backward[j+1] == 1:
                res += 1
            elif j+1 == len(arr) and forward[i-1] == 1:
                res += 1
            elif forward[i-1] == 1 and backward[j+1] == 1 and arr[j+1] > arr[i-1]:
                res += 1
    return res

# define the test case
tasks = [([1, 2, 3], 7), ([1, 2, 3, 4], 11), ([1, 2, 3, 4, 9, 8, 5, 6, 4, 1, 2, 3, 6, 5, 8, 9], 21)]
@pytest.mark.parametrize("arr, ans", tasks)

def test_fn(arr, ans):
    result = countIncresaingMasking(arr)
    assert result == ans

