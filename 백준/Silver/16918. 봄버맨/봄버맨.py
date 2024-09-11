import sys
input = sys.stdin.readline

# 폭탄을 설치하는 함수
def laybomb(grid):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                grid[i][j] = 'O'

# 폭탄을 터뜨리는 함수
def bomb(grid):
    # 폭발을 기록할 임시 리스트를 생성
    new_grid = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                if i > 0:
                    new_grid[i-1][j] = '.'
                if i < r - 1:
                    new_grid[i+1][j] = '.'
                if j > 0:
                    new_grid[i][j-1] = '.'
                if j < c - 1:
                    new_grid[i][j+1] = '.'
    return new_grid

# 입력 받기
r, c, n = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(r)]

if n == 1:
    # 1초 후는 초기 상태 그대로
    for row in grid:
        print(''.join(row))
elif n % 2 == 0:
    # 짝수 초일 때는 모두 폭탄으로 채워짐
    for _ in range(r):
        print('O' * c)
else:
    # 홀수 초일 때는 폭발 후의 상태를 결정
    # 3초 후의 상태
    grid_after_bomb = bomb(grid)
    if n % 4 == 3:
        for row in grid_after_bomb:
            print(''.join(row))
    else:
        # 5초 후의 상태 (한 번 더 폭발)
        grid_after_second_bomb = bomb(grid_after_bomb)
        for row in grid_after_second_bomb:
            print(''.join(row))
