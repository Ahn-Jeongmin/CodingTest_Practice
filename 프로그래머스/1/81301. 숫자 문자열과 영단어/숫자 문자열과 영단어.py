def solution(s):
    ori=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ['0','1','2','3','4','5','6','7','8','9']
    for x, y in zip(ori, answer):
        s=s.replace(x, y)
    return int(s)