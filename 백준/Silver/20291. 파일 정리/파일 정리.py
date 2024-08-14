import sys
input = sys.stdin.readline

filenum = int(input().strip())
filedic = {}
for _ in range(filenum):
    file = input().strip().split('.')
    x = file[1]
    if x in filedic:
        filedic[x] += 1
    else:
        filedic[x] = 1

for key in sorted(filedic.keys()):
    print(f"{key} {filedic[key]}")