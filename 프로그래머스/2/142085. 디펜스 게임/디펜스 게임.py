import heapq
def solution(n, k, enemy):
    answer = 0
    
    heap = []
    
    for e in enemy :
        n = n-e
        heapq.heappush(heap, -e)
        answer +=1
        
        # 7-4 =3
        # 3-2 = 1
        
        if n < 0: # 무적권써버리기
            if k == 0 :
                return answer -1
            
            biggest = heapq.heappop(heap)
            k = k-1
            n = n-biggest
            
    return answer
        
        
    
    
    
    
    
    
    
    
    
    
    return answer