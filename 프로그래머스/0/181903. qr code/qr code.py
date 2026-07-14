def solution(q, r, code):
    answer = ''
    
    for i in range (0, len(code)) :
        target_idx = i % q
        if target_idx == r :
            answer += code[i]
    return answer