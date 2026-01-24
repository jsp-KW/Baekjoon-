from itertools import permutations

def solution(k, dungeons):
    
    answer = -1
    
    # k:현재 피로도
    # 최소>= 소모
    for per in permutations(dungeons):
        now_hp=k
        temp_res=0
        for cur in per: #need,consume
            need, consum = cur
            if now_hp>= need :
                now_hp= now_hp-consum
                temp_res=temp_res+1
            
            else:
                continue
            
            answer= max(answer,temp_res)
            
                
            
    return answer