import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
id_dict = {}
for _ in range(m):
    temp = input().strip().split()
    id_dict[temp[0]] = temp[1]
for _ in range(n):
    temp = input().strip()
    print(id_dict[temp])