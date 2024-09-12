import sys
from collections import deque

input = sys.stdin.readline
testcase = int(input().strip())
queue = deque()

for _ in range(testcase):
    command = list(input().strip().split())
    if command[0] == "push" :
        queue.append(command[1])

    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])