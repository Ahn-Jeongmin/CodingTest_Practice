def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                num = name.index(j)
                score += yearning[num]
            else:
                score += 0
        answer.append(score)
                
    return answer