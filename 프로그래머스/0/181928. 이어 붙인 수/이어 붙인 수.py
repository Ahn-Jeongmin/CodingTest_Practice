def solution(num_list):
    odd_str = ''.join([str(num) for num in num_list if num % 2 != 0])
    even_str = ''.join([str(num) for num in num_list if num % 2 == 0])
    
    odd_num = int(odd_str) if odd_str else 0
    even_num = int(even_str) if even_str else 0
    
    return odd_num + even_num