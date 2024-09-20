import sys
input = sys.stdin.readline

N= int(input().strip())
milk = []
for _ in range(N):
    x = int(input().strip())
    milk.append(x)

answer = 0
milk.sort(reverse = True)
for i in range(len(milk)):
    if (i+1)%3 != 0:
        answer += milk[i]
print(answer)
    
    