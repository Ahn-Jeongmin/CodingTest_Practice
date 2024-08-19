import sys
input = sys.stdin.readline

length = int(input().strip())
numlist = list(map(int, input().strip().split()))

dp = [0] * length

for i in range(length):
    dp[i] = numlist[i]

for i in range(1, length):
    for j in range(i):
        if numlist[i] > numlist[j]:
            dp[i] = max(dp[i], dp[j] + numlist[i])

print(max(dp))