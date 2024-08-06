import heapq
import sys

def process_operations(operations):
    min_heap = []
    results = []

    for x in operations:
        if x != 0:
            heapq.heappush(min_heap, (abs(x), x))
        else:
            if min_heap:
                _, value = heapq.heappop(min_heap)
                results.append(value)
            else:
                results.append(0)

    return results

n = int(sys.stdin.readline().strip())
operations = [int(sys.stdin.readline().strip()) for _ in range(n)]

results = process_operations(operations)

for result in results:
    print(result)
