def solution(a, b):
    new = a*10**len(str(b)) + b
    if new >= 2*a*b:
        return new
    else:
        return 2*a*b