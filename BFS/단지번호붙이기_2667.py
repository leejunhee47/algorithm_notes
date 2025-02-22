"""
1. 아이디어
- bfs이용
- 이중 for문을 돌면서 0이 아닌 수를 발견하면 bfs 실행
- 단지수를 출력
- 집의 개수 출력
2. 시간복잡도
- V = N * N = 625
- E = 625 * 4 = 2500
- V + E < 2억 가능
3. 자료구조
- map int[][]
- 방문 int[][]
- 단지 수, 집 수
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    houses = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if map[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    houses += 1
    return houses


villages = 0
house_num = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and visited[i][j] == False:
            house_num.append(bfs(i, j))
            villages += 1
house_num.sort()
print(villages)
for a in house_num:
    print(a)