import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(node, graph, visited, order, count):
    visited[node] = True
    order[node] = count
    count += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count = dfs(neighbor, graph, visited, order, count)
    return count

def main():
    data = input().splitlines()
    N, M, R = map(int, data[0].split())
    
    graph = [[] for _ in range(N + 1)]
    for i in range(1, M + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    for neighbors in graph:
        neighbors.sort()
    
    visited = [False] * (N + 1)
    order = [0] * (N + 1)
    
    dfs(R, graph, visited, order, 1)
    
    for i in range(1, N + 1):
        print(order[i])

if __name__ == "__main__":
    main()

