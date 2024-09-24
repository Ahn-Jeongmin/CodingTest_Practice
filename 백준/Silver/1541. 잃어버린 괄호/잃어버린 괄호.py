import sys
input = sys.stdin.readline().strip

equation = input()
minuslist = equation.split("-")
for i in range(len(minuslist)):
    x = list(map(int, minuslist[i].split("+")))
    minuslist[i] = sum(x)
    
answer = minuslist[0]
for i in range(1, len(minuslist)):
    answer -= minuslist[i]

print(answer)    
     