"""
1. 아이디어
- 이진 탐색
- 처음 리스트에서 숫자 하나 뽑아서 이진 탐색
- 두번째 리스트를 오름차순 정렬해서 탐색
2. 시간복잡도
- log10만 < 2억
3. 자료구조
- 수열 int[] int[]
"""

import sys
input = sys.stdin.readline

def binary_search(array, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort() # 오름차순 정렬

for b in B:
    if binary_search(A, 0, n-1, b) is None:
        print(0)
    else:
        print(1)



