import sys
input = sys.stdin.readline

n = int(input().strip())
numlist = list(map(int, input().strip().split()))

answer = 0
suffix_sum = 0

for i in range(n-1, -1, -1):
    answer += numlist[i] * suffix_sum
    suffix_sum += numlist[i]

print(answer)

