"""
1. 아이디어
- 다익스트라 알고리즘을 돌면서
- i번째 줄에 i번 정점의 최단 경로 출력
- 경로가 존재하지 않으면 INF 출력
2. 시간복잡도
- O(ElogV)
- 3e5 * log2e4 < 2억
- 가능
3. 자료구조
- graph, visited, distance int[]
- heapq int[]
"""
import heapq
import sys



input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())
visited = [False] * (v+1)
distance = [1e9] * (v+1)
# 방문처리
visited[k] = True

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



dijkstra(k)

for i in range(1, v+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])