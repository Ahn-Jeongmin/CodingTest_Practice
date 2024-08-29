import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, start, root):
    for i in graph[start]:
        if root[i]==0:
            root[i]=start
            dfs(graph, i, root)
    return root

nodenum = int(input().strip())

graph = [[] for _ in range(nodenum+1)]

for _ in range(nodenum-1):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)
root = [0]*(nodenum + 1)

dfs(graph, 1, root) 

for x in range(2, nodenum+1):
    print(root[x])