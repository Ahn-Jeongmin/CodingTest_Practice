a_len, b_len = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = a+b
answer.sort()

for i in range(a_len+b_len):
    if i < a_len+b_len-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])