def solution(s, n):
    slist=list(s)
    for i in range(0,len(slist)):
        if slist[i]==' ':
            continue
        elif ((ord(slist[i])+n)>90 and slist[i].isupper()) or ((ord(slist[i])+n)>122 and slist[i].islower()):
            slist[i]=chr(ord(slist[i])+n-26)
        else:
            slist[i]=chr(ord(slist[i])+n)
    answer=''.join(slist)
    return answer