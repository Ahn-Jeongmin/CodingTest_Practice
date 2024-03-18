def solution(brown, yellow):
    answer = []
    yellow_c = []

    # yellow 타일의 조합 확인
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            if (i * 2 + (yellow//i) * 2 + 4) == brown:
                answer = [(yellow//i) + 2, i + 2]
    return answer