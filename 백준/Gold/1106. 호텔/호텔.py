C, N = map(int, input().split())  
city = []

for _ in range(N):
    cost, customers = map(int, input().split())
    city.append((cost, customers))

max_cost = float('inf')
dp = [max_cost] * (C + 101)  

dp[0] = 0
for cost, customers in city:
    for i in range(customers, C + 101):
        dp[i] = min(dp[i], dp[i - customers] + cost)


min_cost = min(dp[C:C + 101])
print(min_cost)