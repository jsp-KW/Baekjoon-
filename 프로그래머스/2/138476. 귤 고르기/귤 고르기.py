from collections import Counter 

def solution(k, tangerine):
    
    answer = 0
    counter = Counter(tangerine)
    
    counts = sorted(counter.values(), reverse= True)
    # 귤 종류 최소 개수여야함.
    
    type_cnt = 0
    weight_sum = 0
    for cnt in counts:
        if weight_sum >= k :
            break
        weight_sum += cnt
        type_cnt +=1 
        
    answer= type_cnt
        
    
    
    
    return answer