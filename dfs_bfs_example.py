def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리를 이용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
		    # 큐에서 하나의 원소를 뽑아 출력하기
		    v = queue.popleft()
		    print(v, end=' ')
		    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
		    for i in graph[v]:
		        if not visited[i]:
		            queue.append(i)
		            visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
] 

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 1부터 시작하기 위해서 9로 설정
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
