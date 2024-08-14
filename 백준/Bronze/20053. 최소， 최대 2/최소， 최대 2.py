import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    num = int(input())
    x = list(map(int, input().split()))
    print(min(x), max(x))