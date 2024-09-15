import sys
input = sys.stdin.readline

num = int(input().strip())
stair = [0]
dp = [0]*(num+1)
for _ in range(num):
    temp = int(input().strip())
    stair.append(temp)

for i in range(1, num+1):
    if i==1:
        dp[1] = stair[1]
    elif i==2:
        dp[2] = stair[1]+stair[2]
    else:
        one = dp[i-2] + stair[i]
        two = dp[i-3] + stair[i-1] + stair[i]
        dp[i] = max([one, two])
    
print(dp[-1])