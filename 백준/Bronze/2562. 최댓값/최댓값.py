numlist = []
for _ in range(9):
    x = int(input())
    numlist.append(x)
answer = max(numlist)
print(answer)
print(numlist.index(answer)+1)