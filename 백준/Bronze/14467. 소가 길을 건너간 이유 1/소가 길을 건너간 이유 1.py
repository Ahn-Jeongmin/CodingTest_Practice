import sys
input = sys.stdin.readline

observe = int(input())
answer = 0
cowlist = [-1]*10
for _ in range(observe):
    cowindex, point = map(int, input().split())
    if cowlist[cowindex-1]==-1:
        cowlist[cowindex-1] = point
    elif cowlist[cowindex-1]!=point:
        cowlist[cowindex-1] = point
        answer += 1
    else:
        continue
        

print(answer)