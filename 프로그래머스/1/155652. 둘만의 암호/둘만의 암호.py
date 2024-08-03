def solution(s, skip, index):
    skip_set = set(skip)
    
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    available_letters = [ch for ch in alphabet if ch not in skip_set]
    
    result = []
    
    for char in s:
        current_index = available_letters.index(char)
        new_index = (current_index + index) % len(available_letters)
        result.append(available_letters[new_index])
    
    return ''.join(result)

