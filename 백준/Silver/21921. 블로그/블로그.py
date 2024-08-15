import sys
input = sys.stdin.readline

day, period = map(int, input().strip().split())
visitorlist = list(map(int, input().strip().split()))
currentsum = sum(visitorlist[0:period])
maxsum = currentsum
count = 1

for i in range(1,day-period+1):
    currentsum = currentsum - visitorlist[i-1] + visitorlist[i+period-1]
    if currentsum>maxsum:
        maxsum = currentsum
        count = 1
    elif currentsum == maxsum:
        count+=1
    
    
if maxsum == 0:
    print("SAD")
else:
    print(maxsum)
    print(count)
    
    