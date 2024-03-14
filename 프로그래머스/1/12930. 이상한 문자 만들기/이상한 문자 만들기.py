def solution(s):
    answer_list=[]
    word=s.split(' ')
    for i in word:
        answer = list(i)
        for j in range(0, len(answer)):
            if j%2==0:
                answer[j]=answer[j].upper()
            else:
                answer[j]=answer[j].lower()
        answer_list.append(''.join(answer))
                
    return ' '.join(answer_list)