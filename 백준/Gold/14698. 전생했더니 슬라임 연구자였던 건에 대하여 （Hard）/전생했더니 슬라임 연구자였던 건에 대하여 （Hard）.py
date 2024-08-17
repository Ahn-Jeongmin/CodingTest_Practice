import sys
input = sys.stdin.readline

testcase = int(input().strip())
for _ in range(testcase):
    answer = 1
    slimenum = int(input().strip())
    slimelist = list(map(int,input().strip().split()))
    if slimenum == 1:
        answer=1
    else:
        for i in range(slimenum-1):
            slimelist.sort()
            x = slimelist[0]*slimelist[1]
            answer *= x
            if i == slimenum-2:
                continue
            else:
                slimelist = [x]+slimelist[2:]
        
    print(answer%1000000007)