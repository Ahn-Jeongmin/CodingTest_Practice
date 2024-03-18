def solution(n):
    answer = 0
    Fib=[]
    Fib.append(0)
    Fib.append(1)
    
    if n>=2:
        for i in range(2, n+1):
            temp=Fib[i-2] + Fib[i-1]
            Fib.append(temp)
    
    temp=Fib[n]
    answer=temp%1234567
    
    return answer
