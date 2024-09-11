from collections import deque
M, N = map(int, input().split())
arr = []
queue = deque()
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 1: #익은 토마토 덱에 위치 넣기
            queue.append((i, j))

d = d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def bfs():  
    while queue: #토마토 다 익힐때까지 반복 (0없애기)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0: #다음 위치가 안익은 토마토이면 익혀나가기
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny)) #이것도 익은거니까 덱에 위치 넣기
bfs()
def get_day():
    result = 0 #결과
    for row in arr:
        if 0 in row: 
            return -1

        row_max = max(row)    
        if result < row_max:
            result = row_max
    return result - 1 
print(get_day())
