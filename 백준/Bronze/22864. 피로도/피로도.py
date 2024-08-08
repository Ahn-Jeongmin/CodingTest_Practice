x = list(map(int, input().split()))
fatigue = 0
work = 0

for _ in range(24):
    if fatigue + x[0] > x[3]:
        fatigue -= x[2]
        if fatigue<0 :
            fatigue = 0
    else:
        fatigue += x[0]
        work += x[1]
    
print(work)