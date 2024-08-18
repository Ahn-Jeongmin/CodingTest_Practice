import sys
input = sys.stdin.readline

length = int(input().strip())
numlist = list(map(int, input().strip().split()))
maxlist = [numlist[0]]
for i in range(1, length):
    maxlist.append(max(numlist[i], maxlist[i-1] + numlist[i]))

print(max(maxlist))
