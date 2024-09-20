def solution(babbling):
    valid_babbles = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for word in babbling:
        for babble in valid_babbles:
            if babble in word:
                word = word.replace(babble, " ")
        word = word.replace(" ", "")
        if word == "":
            answer += 1
            
    return answer
