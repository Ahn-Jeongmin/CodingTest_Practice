import sys

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True
    countnum = 0

    while stack:
        node = stack.pop()
        countnum += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return countnum

input = sys.stdin.readline
comnum, relation = map(int, input().strip().split())

graph = [[] for _ in range(comnum+1)]
for _ in range(relation):
    x, y = map(int, input().strip().split())
    graph[y].append(x)

visited = [False]*(comnum+1)

answer = [0]*(comnum+1)
for i in range(1, comnum+1):
    visited = [False]*(comnum+1)
    x = dfs(graph, i, visited)
    answer[i] = x

maxnum = max(answer)
for i in range(1, comnum+1):
    if answer[i] == maxnum:
        print(i, end=" ")
