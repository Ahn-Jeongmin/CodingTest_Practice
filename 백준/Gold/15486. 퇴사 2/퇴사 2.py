import sys
input = sys.stdin.readline

day = int(input().strip())
daylist = []
for _ in range(day):
    t, p = map(int, input().strip().split())
    daylist.append([t, p])

dp = [0] * (day + 1)

for i in range(day - 1, -1, -1):
    if i + daylist[i][0] > day: 
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], daylist[i][1] + dp[i + daylist[i][0]])

print(dp[0])

    