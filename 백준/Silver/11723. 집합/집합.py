import sys
input = sys.stdin.readline

test = int(input().strip())
s = []
for _ in range(test):
    x = input().strip().split()
    if x[0] == "add":
        if int(x[1]) not in s:
            s.append(int(x[1]))
            
    elif x[0] == "remove":
        if int(x[1]) in s:
            s.remove(int(x[1]))
            
    elif x[0] == "check":
        if int(x[1]) in s:
            print(1)
        else:
            print(0)
            
    elif x[0] == "toggle":
        if int(x[1]) in s:
            s.remove(int(x[1]))
        else:
            s.append(int(x[1]))
            
    elif x[0] == "all":
        s = [i for i in range(1, 21)]
        
    elif x[0] == "empty":
        s = []
    
            