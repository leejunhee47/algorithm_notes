"""
1. 아이디어
- bfs
- 이중 for 1 && 방문 x
- 그림 넓이 count
2. 시간복잡도
- V = N * N = 250000
- E = 4N^2= 1000000
- V + E < 2억 가능
3. 자료구조
- map int[][]
- 방문 int[][]
- 넓이
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        # print('x', x, 'y', y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if pictures[nx][ny] == 1 and visited[nx][ny] == False:
                    # print('append', nx, ny)
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count



result = []
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1 and visited[i][j] == False:
            result.append(bfs(i, j))
if len(result) == 0:
    print(0)
    print(0)
else:
    print(len(result))
# print('result', result)
    print(max(result))