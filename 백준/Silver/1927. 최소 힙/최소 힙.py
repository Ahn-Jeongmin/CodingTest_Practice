import sys
import heapq

input = sys.stdin.readline
testcase = int(input().strip())
q = []

for _ in range(testcase):
    num = int(input().strip())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)
