import sys
input = sys.stdin.readline

N = int(input())
target = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dxdyping = 0
movenum = 1
snail = [N//2, N//2]
grid = [[0]*N for _ in range(N)]
grid[N//2][N//2] = 1
number = 2
answer = [N//2+1, N//2+1]     

flag = True
while number <= N*N:
    for _ in range(2):  
        for _ in range(movenum):
            snail[0] += dy[dxdyping]
            snail[1] += dx[dxdyping]

            if 0 <= snail[0] < N and 0 <= snail[1] < N:
                grid[snail[0]][snail[1]] = number
                if number == target:
                    answer = [snail[0] + 1, snail[1] + 1]

            number += 1
            if number > N*N:
                break  
        if number > N*N:
                break 
        dxdyping = (dxdyping + 1) % 4
    movenum += 1

for i in range(N):
    print(*grid[i])

print(*answer)