"""
1. 아이디어
- 계수정렬 사용
- 리스트에 해당 정수가 몇번 나오는지 저장하고
- 구하려는 정수의 개수를 출력
2. 시간복잡도
- O(N+K)
- 500000 + 20000000 < 2억
- 가능
3. 자료구조
- 정수 저장 int [][]
- n, m
"""

n = int(input())

arr = list(map(int, input().split()))

tmp = [0] * 20000001

for num in arr:
    tmp[num] += 1

m = int(input())
find = list(map(int, input().split()))
for i in find:
    # print('i', i)
    print(tmp[i], end=' ')