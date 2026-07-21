def solution(my_strings, parts):
    answer = ''
    
    for i in range (0, len(parts)):
        start_idx = parts[i][0]
        end_idx = parts[i][1]
        target= my_strings[i]
        temp = target[start_idx : end_idx +1]
    
        for ch in temp :
            answer+= ch
    
    
    return answer