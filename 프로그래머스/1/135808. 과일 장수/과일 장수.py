def solution(k, m, score):
    answer = 0
    
    score.sort (reverse= True)

    
    can_make_box = len(score) // m
    idx=0
    while can_make_box >0 :
        target = score[idx:idx+m]
        min_val = target[m-1]
        answer += (min_val *m)
        idx =idx +m
        can_make_box -=1
            
    return answer