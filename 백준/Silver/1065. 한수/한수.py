import sys
input  = sys.stdin.readline

maxnum = int(input())
count = 99
if maxnum < 100 :
    print(maxnum)
elif maxnum == 1000:
    print(144)
else:
    for i in range(100, maxnum + 1):
        hund = i//100
        ten = (i%100)//10
        one = i%10
        
        if (hund - ten) == (ten - one):
            count += 1
    print(count)
        