def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                score += dictionary[j]
            else:
                score += 0
        answer.append(score)
                
    return answer