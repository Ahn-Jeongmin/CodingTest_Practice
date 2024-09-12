for _ in range(3):
    N = int(input())  
    total_sum = 0    
    for _ in range(N):
        num = int(input())
        total_sum += num   
    if total_sum > 0:
        print("+")
    elif total_sum < 0:
        print("-")
    else:
        print("0")
