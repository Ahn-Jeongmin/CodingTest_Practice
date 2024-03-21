def solution(clothes):
    answer = 1
    num_list=[]
    cloth_list=[]
    for i in clothes:
        if i==clothes[0] or i[1] not in cloth_list:
            cloth_list.append(i[1])
            num_list.append(1)
        else:
            target_index=cloth_list.index(i[1])
            num_list[target_index]+=1
    for i in num_list:
            answer*=(i+1)
    return answer-1