import sys
input = sys.stdin.readline

N = int(input().strip())
energy = list(map(int, input().strip().split()))
answer = max(energy)
energy.remove(answer)
for i in energy:
    answer += i/2

print(answer)