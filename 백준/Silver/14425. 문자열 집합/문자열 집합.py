def countword():
    num = list(map(int,input().split()))
    wordlist = []
    answer = 0
    for i in range(num[0]):
        temp = input()
        wordlist.append(temp)
    
    for i in range(num[1]):
        temp = input()
        if temp in wordlist:
            answer += 1
                
    return answer
        
print(countword())