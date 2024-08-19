def solution(a, b):
    new1 = b*10**len(str(a)) + a
    new2 = a*10**len(str(b)) + b
    return max(new1, new2)