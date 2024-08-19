import sys
input = sys.stdin.readline

testcase = int(input().strip())
for _ in range(testcase):
    a, b = map(int, input().strip().split())
    a = list(str(a))
    b = list(str(b))
    if len(a) > len(b):
        b = ['0'] * (len(a) - len(b)) + b
    else:
        a = ['0'] * (len(b) - len(a)) + a
    
    answer = []
    carry = 0 
    for i in range(len(a) - 1, -1, -1):
        sum_val = int(a[i]) + int(b[i]) + carry
        if sum_val == 0:
            answer.append('0')
            carry = 0
        elif sum_val == 1:
            answer.append('1')
            carry = 0
        elif sum_val == 2:
            answer.append('0')
            carry = 1
        elif sum_val == 3:
            answer.append('1')
            carry = 1
    
    if carry == 1:
        answer.append('1')
    
    answer.reverse()
    print(''.join(answer))
