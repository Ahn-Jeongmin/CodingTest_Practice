import math
def solution(progresses, speeds):
    answer = []
    for i in range(0, len(progresses)):
        progresses[i]=math. ceil((100-progresses[i])/speeds[i])
    for i in range(0, len(progresses)-1):
        if progresses[i]>progresses[i+1]:
            progresses[i+1]=progresses[i]
    top=0
    answernum=1
    for i in range(0, len(progresses)):
        if i==0:
            top=progresses[i]
            
        elif progresses[i]==top:
            answernum+=1
        else:
            answer.append(answernum)
            top=progresses[i]
            answernum=1
        if i==len(progresses)-1:
            answer.append(answernum)
    return answer