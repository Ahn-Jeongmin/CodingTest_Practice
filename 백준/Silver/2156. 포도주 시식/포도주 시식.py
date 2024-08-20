grapenum=int(input())
grapelist=[0]*grapenum
for i in range(grapenum):
    grapelist[i]=int(input())

if grapenum == 0:
    print(0)
elif grapenum == 1:
    print(grapelist[0])
elif grapenum == 2:
    print(grapelist[0] + grapelist[1])
else:
    dp = [0] * grapenum
    dp[0] = grapelist[0]
    dp[1] = grapelist[0] + grapelist[1]
    dp[2] = max(grapelist[2] + grapelist[0], grapelist[2] + grapelist[1], dp[1])

    for i in range(3, grapenum):
        dp[i] = max(grapelist[i] + dp[i-2], grapelist[i] + grapelist[i-1] + dp[i-3], dp[i-1])
    print(max(dp))