import heapq
def solution(k, score):
    answer = []
    temp = []
    
    day = 1
    
    for current_score in score :
        if day > k : 
            if len(temp) == k : 
                cur_min_val = temp[0]
                if cur_min_val < current_score :
                    heapq.heappush (temp, current_score)
                    heapq.heappop(temp)
                
                    
        else: 
            heapq.heappush(temp, current_score)   
        
        day +=1
        answer.append(temp[0])
    
    
    return answer