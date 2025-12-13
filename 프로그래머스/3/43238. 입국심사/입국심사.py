def solution(n, times):
    answer = 0
    
    # n 명이 심사를 받는데 걸리는 시간의 최솟값을 return 
    # T라 하고, 심사시간이 t인 심사관은
    # 0~t, t~2t, 해서 T//t 명 처리가 가능하다,
    # 즉, T//times[i] 의 합인데,
    
    low  = min(times)
    high = min(times)*n
    
    while low < high :
        T = (low+high) // 2
        
        processed = 0
        
        for t in times :
            processed += T//t 
            if processed>= n :
                break
        
        if processed >= n :
            high = T
        else:
            low = T+1
            
            
        
    
    return low