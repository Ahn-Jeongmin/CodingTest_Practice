import sys
input= sys.stdin.readline

num = int(input().strip())
fiblist = [0]*(num+1)

fiblist[0] = 0
fiblist[1] = 1
if num > 1:
    for i in range(2, num+1):
        fiblist[i] = fiblist[i-1] + fiblist[i-2]
        
print(fiblist[num])
    
