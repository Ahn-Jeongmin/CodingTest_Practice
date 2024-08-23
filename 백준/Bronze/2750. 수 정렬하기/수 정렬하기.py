num = int(input())
numlist=[]
for _ in range(num):
    x = int(input())
    numlist.append(x)
numlist.sort()
for i in range(num):
    print(numlist[i])
    