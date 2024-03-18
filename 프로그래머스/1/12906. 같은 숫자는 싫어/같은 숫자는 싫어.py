def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr[1:]:
        top=answer[-1]
        if i!=top:
            answer.append(i)
    return answer