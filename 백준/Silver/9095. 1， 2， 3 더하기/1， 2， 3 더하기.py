import sys
input = sys.stdin.readline

testcase = int(input().strip())
for _ in range(testcase):
    num = int(input().strip())
    numlist = [1, 2, 4, 7]
    if num > 4:
        for i in range(4, num): 
            x = numlist[i-1] + numlist[i-2] + numlist[i-3]
            numlist.append(x)
    print(numlist[num-1])
    