def solution(n, m, section):
    answer = 0
    
    # n길이가 n
    # 룰러 m 미터, 
    #
    
    end_idx=0
    for s in section:
        if s >=end_idx :
            answer+=1
            end_idx = s+m
        
                          
    return answer