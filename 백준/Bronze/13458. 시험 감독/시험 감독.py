def supervisor():
    a = int(input())
    student_in_class = list(map(int, input().split()))
    c = input().split()
    c_cap = int(c[0])
    c_sub = int(c[1])
    answer = 0
    
    for i in student_in_class:
        if i-c_cap<0:
            answer += 1
        else:
            x=1
            if (i-c_cap) % (c_sub) != 0:
                answer += (i-c_cap) // (c_sub) + 2
            else:
                answer += (i-c_cap) // (c_sub) + 1
                
    return answer

print(supervisor())