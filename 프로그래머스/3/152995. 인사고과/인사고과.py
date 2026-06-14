def solution(scores):
    answer = 0
    
    # 4 5 5 5 3
    
    wanho_sum = scores[0][0] + scores[0][1]
    
    wanho = scores[0] 
    
    scores.sort(key= lambda x : (-x[0],x[1]))
    max_peer = 0 
    rank = 1
    
    
    for attitude, peer in scores :
        if peer < max_peer :
            if attitude == wanho[0] and peer == wanho[1] :
                return -1
            continue 
            
        max_peer = max(max_peer, peer)
        
        if attitude + peer >  wanho_sum :
            rank+=1
            
    return rank