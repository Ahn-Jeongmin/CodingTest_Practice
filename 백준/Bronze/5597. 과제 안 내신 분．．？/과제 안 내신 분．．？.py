studentlist = [i for i in list(range(1,31))]
for _ in range(28):
    x = int(input())
    studentlist.remove(x)
studentlist.sort()
print(studentlist[0])
print(studentlist[1])