def solution(my_string):
    count_array = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':  
            index = ord(char) - ord('A')
            count_array[index] += 1
        elif 'a' <= char <= 'z':  
            index = ord(char) - ord('a') + 26
            count_array[index] += 1
    
    return count_array
