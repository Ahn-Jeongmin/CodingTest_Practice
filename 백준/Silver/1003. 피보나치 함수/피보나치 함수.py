import sys
input = sys.stdin.readline

def fib_count01(num):
    if num == 0:
        return 1,0
    elif num == 1:
        return 0, 1
    fiblist_zero = [1, 0]
    fiblist_one = [0, 1]    
    for i in range(2, num+1):
        fiblist_zero.append(fiblist_zero[-1]+fiblist_zero[-2])
        fiblist_one.append(fiblist_one[-1]+fiblist_one[-2])
            
    return fiblist_zero[num], fiblist_one[num]
    
testcase = int(input())

for i in range(testcase):
    num = int(input())
    zero, one = fib_count01(num)
    print(zero, one)