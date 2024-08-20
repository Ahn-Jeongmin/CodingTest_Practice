import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coinlist = []
for _ in range(n):
    x = int(input().strip())
    coinlist.append(x)
coinlist.sort()

dp = [float('inf')] * (k + 1)
dp[0] = 0 

for coin in coinlist:
    for j in range(coin, k + 1):
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
