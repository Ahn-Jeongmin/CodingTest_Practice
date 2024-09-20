import sys
input = sys.stdin.readline

N = int(input())
Plist = list(map(int, input().strip().split()))

Plist.sort(reverse = True)
summation = 0
for i in range(len(Plist)):
    summation += sum(Plist[i:])
print(summation)