import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
fact = [1]

for i in range(1, n+1):
    fact.append(fact[i-1]*i)
    
answer = fact[n]//(fact[m]*fact[n-m])
print(answer)