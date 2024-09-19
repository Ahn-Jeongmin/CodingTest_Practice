def solution(N, stages):
    answer = []
    people = len(stages)
    notsolved = [0]*(N+2)
    notsolved[0] = -1
    for i in stages:
        if i != N+1:
            notsolved[i] += 1
    
    for i in range(1, len(notsolved)):
        x = notsolved[i]
        if people > 0:
            notsolved[i] = x / people
        else:
            notsolved[i] = 0
        people -= x
    
    for _ in range(len(notsolved)-2):
        x = notsolved.index(max(notsolved))
        answer.append(x)
        notsolved[x] = -1
        
    return answer
