while(True):
    x = list(map(int, input().split()))
    if x[0]==0 and x[1]==0:
        break
    elif x[0] > x[1]:
        print("Yes")
    else:
        print("No")