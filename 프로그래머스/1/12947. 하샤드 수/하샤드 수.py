def solution(x):
    answer = True
    xlist=list(map(int, list(str(x))))
    xsum=sum(xlist)
    if x%xsum==0:
        return True
    else:
        return False