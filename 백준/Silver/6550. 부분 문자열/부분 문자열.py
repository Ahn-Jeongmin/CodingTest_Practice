import sys
input = sys.stdin.readline
while True:
    line = input().strip()
    if not line:
        break  
    S, T = line.split()
    
    flag = 0
    for i in T:
        if i == S[flag]:
            flag += 1
        if flag >= len(S):
            print("Yes")
            break
        
    if flag < len(S):
        print("No")