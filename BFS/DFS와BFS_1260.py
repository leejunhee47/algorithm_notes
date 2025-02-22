import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
# print(n, m, start)
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (n+1)
visited2 = visited.copy()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)

def bfs(v):
    q = [v]
    visited2[v] = True
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i] == False and graph[v][i] == 1:
                q.append(i)
                visited2[i] = True
dfs(start)
print()
bfs(start)


