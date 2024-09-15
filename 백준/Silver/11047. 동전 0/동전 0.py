import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
money = []
for _ in range(n):
    x = int(input().strip())
    money.append(x)
money.sort(reverse= True)
moneycount = 0
for i in money:
    moneycount += k//i
    k = k%i
print(moneycount)