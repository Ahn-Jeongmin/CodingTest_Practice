def solution(survey, choice):
    answer = ''
    #RT" "FC, "MJ" "AN"
    temper = [[0,0], [0,0], [0,0], [0,0]]
    for i in range(len(survey)):
        #RT
        if survey[i] == "RT":
            if choice[i]>4:
                temper[0][1] += choice[i]-4
            elif choice[i]< 4:
                temper[0][0] += 4-choice[i]
        elif survey[i] == "TR":
            if choice[i]>4:
                temper[0][0] += choice[i]-4
            elif choice[i]< 4:
                temper[0][1] += 4-choice[i]
        #FC 
        elif survey[i] == "CF":
            if choice[i]>4:
                temper[1][1] += choice[i]-4
            elif choice[i]< 4:
                temper[1][0] += 4-choice[i]
        elif survey[i] == "FC":
            if choice[i]>4:
                temper[1][0] += choice[i]-4
            elif choice[i]< 4:
                temper[1][1] += 4-choice[i]
                
        #MJ
        elif survey[i] == "JM":
            if choice[i]>4:
                temper[2][1] += choice[i]-4
            elif choice[i]< 4:
                temper[2][0] += 4-choice[i]
        elif survey[i] == "MJ":
            if choice[i]>4:
                temper[2][0] += choice[i]-4
            elif choice[i]< 4:
                temper[2][1] += 4-choice[i]
        #AN
        elif survey[i] == "AN":
            if choice[i]>4:
                temper[3][1] += choice[i]-4
            elif choice[i]< 4:
                temper[3][0] += 4-choice[i]
        elif survey[i] == "NA":
            if choice[i]>4:
                temper[3][0] += choice[i]-4
            elif choice[i]< 4:
                temper[3][1] += 4-choice[i]
       #RT" "CF, "JM" "AN"  
    if temper[0][0]>=temper[0][1]:
        answer += "R"
    elif temper[0][0]<temper[0][1]:
        answer+="T"
        
    if temper[1][0]>=temper[1][1]:
        answer += "C"
    elif temper[1][0]<temper[1][1]:
        answer+="F"
    
    if temper[2][0]>=temper[2][1]:
        answer += "J"
    elif temper[2][0]<temper[2][1]:
        answer+="M"
        
    if temper[3][0]>=temper[3][1]:
        answer += "A"
    elif temper[3][0]<temper[3][1]:
        answer+="N"
                
                
    return answer