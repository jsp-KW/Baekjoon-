def solution(n, stations, w):
    answer = 0
    coverage = 2*w +1

    # 2w +1 
    
    start  = 1
    end = n
    
    for station in stations :
        left = station -w 
        right = station +w 
        
        if start < left :
            gap = left - start 
            if gap % coverage !=0:
                answer += (gap // coverage ) +1
            else:
                answer += (gap//coverage)
        start = right +1
        
    
    if start <= n :
        gap = n- start +1 
        if gap % coverage  !=0 :
            answer += (gap // coverage ) +1
        else :
            answer += (gap//coverage)
    return answer
        
  