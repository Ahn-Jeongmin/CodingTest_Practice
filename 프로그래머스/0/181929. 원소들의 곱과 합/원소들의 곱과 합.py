def solution(num_list):
    summation = sum(num_list)**2
    mul = 1
    for i in num_list:
        mul*=i
    if mul<summation:
        return 1
    else:
        return 0