# Algorithm: Count Increasing masking

## Overview
給定一個array，刪除某個subarray後，剩餘的element為嚴格遞增。請問有幾種刪除方法?
備註: 單元素以及空集合仍視為嚴格遞增

## Features
Brute Force O(N**3):
-  窮舉所有可以刪除的區間。(N**2)
    -  檢查剩餘的數列是否為嚴格遞增。(N)

Hashmap O(N**2)
-  建構有效遞增序列標記函數，由左到右掃描，函數命名forward (N)
    -  arr = [1, 2, 3, 2]，Forward = [1, 1, 1, 0]
-  建構有效遞減序列標記函數，由右到左掃描，函數命名backward (N)
    -  arr = [1, 2, 1, 2]，Backward = [0, 0, 1, 1]
-  窮舉所有可以刪除的區間[i, j]。(N**2)
    -  利用forward以及backward序列查找刪除區間的兩側位置是否滿足遞增序列。(1)
    -  成立條件一: i=0 且 j=len(arr)。
    -  成立條件二: i=0 且 backend[j + 1]=1。
    -  成立條件三: j=len(arr) 且 forward[i - 1]=1。 。
    -  成立條件四: i>0 且 j < len(arr) 且 backend[j + 1]= 1 且 backend[j + 1]=1 且 arr[j + 1] > arr[i - 1]。

```python
# Example code
pytest "brute force O(N3).py"
pytest "hashmap O(N2).py"