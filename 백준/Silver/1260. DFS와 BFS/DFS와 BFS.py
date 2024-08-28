from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
bfs(graph, v)

    