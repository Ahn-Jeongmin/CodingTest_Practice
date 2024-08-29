import sys
input = sys.stdin.readline

def dfs(graph, node, visited, dfslist):
    visited[node] = True
    dfslist.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, dfslist)

comnum = int(input().strip())
netnum = int(input().strip())
graph = [[] for _ in range(comnum + 1)]

for _ in range(netnum):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (comnum + 1)
dfslist = []
start = 1

dfs(graph, start, visited, dfslist)
print(len(dfslist) - 1)  # Excluding the start node itself
