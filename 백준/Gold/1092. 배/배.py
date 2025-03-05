"""
1. 아이디어
- 크레인과 박스를 내림차순 정렬
- 박스를 큐에 넣고 무게 무거운 순서대로 큐를 popleft
- 만약 무게 제한보다 무거운 박스가 나오면 popleft해서 append
- 한 사이클 돌았는데 pop된게 없으면 -1 출력
2. 시간복잡도
- O(N*M^2) 최악
- O(N*M) 평균

3. 자료구조
- 박스 큐 int[]
- 크레인 int[]
"""

import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)


count = 0
if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()

while len(boxes)>0:

    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    # 한 사이클 돌면 +1
    count += 1

print(count)

"""
2
1 2
4
1 1 2 2
"""