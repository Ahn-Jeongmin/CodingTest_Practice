def solution(N, stages):
    answer = []
    people = len(stages)
    notsolved = [0]*(N+2)
    
    for i in stages:
        if i <= N:  
            notsolved[i] += 1
    
    failure_rates = []
    people_remaining = people
    
    for i in range(1, N + 1):
        if people_remaining > 0:
            failure_rate = notsolved[i] / people_remaining
            people_remaining -= notsolved[i]  
        else:
            failure_rate = 0
        failure_rates.append((i, failure_rate))
        
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [stage for stage, _ in failure_rates]
    
    return answer
