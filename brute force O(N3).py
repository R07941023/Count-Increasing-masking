import pytest
from typing import List

def countIncresaingMasking(arr: List[int]) -> int:

    def checkArrayIncrease(arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True

    res = 0
    if checkArrayIncrease(arr):
        res += 1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            case = arr[:i]+arr[j+1:]
            state = checkArrayIncrease(case)
            if state:
                res +=1
    return res

# define the test case
tasks = [([1, 2, 3], 7), ([1, 2, 3, 4], 11), ([1, 2, 3, 4, 9, 8, 5, 6, 4, 1, 2, 3, 6, 5, 8, 9], 21)]
@pytest.mark.parametrize("arr, ans", tasks)

def test_fn(arr, ans):
    result = countIncresaingMasking(arr)
    assert result == ans

