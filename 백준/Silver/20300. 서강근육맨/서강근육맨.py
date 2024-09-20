import sys
input = sys.stdin.readline

N = int(input().strip())
loss = list(map(int, input().strip().split()))

loss.sort()

sumlist = []

if N % 2 != 0:
    sumlist.append(loss[-1])
    loss.pop()
    N -= 1

for i in range(N // 2):
    sumlist.append(loss[i] + loss[N - i - 1])

print(max(sumlist))
