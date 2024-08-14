import sys
input = sys.stdin.readline

total_bulb_num, command = map(int, input().split())
current_bulb_stat = list(map(int, input().split()))
for _ in range(command):
    command_num, x1, x2 = map(int, input().split())
    if command_num == 1:
        current_bulb_stat[x1-1] = x2
    elif command_num == 2:
        for i in range(x1-1, x2):
            if current_bulb_stat[i]==1:
                current_bulb_stat[i]=0
            else:
                current_bulb_stat[i]=1
    elif command_num == 3:
        for i in range(x1-1, x2):
            current_bulb_stat[i]=0
    else:
        for i in range(x1-1, x2):
            current_bulb_stat[i]=1
    
print(*current_bulb_stat)