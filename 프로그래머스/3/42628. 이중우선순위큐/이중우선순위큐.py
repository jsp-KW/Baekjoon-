import heapq

def solution(operations):
    max_hq = []
    min_hq = []
    isLive =  [False] *(1000001)
    
    def clean_max (max_hq,isLive) :
        while max_hq and not isLive[max_hq[0][1]]  :
            heapq.heappop(max_hq)
        
    def clean_min (min_hq, isLive) :
        while min_hq and not isLive[min_hq[0][1]] :
            heapq.heappop(min_hq) 

        
    for i,op in enumerate(operations) :
        operation, num = op.split()[0], int(op.split()[1])
        if operation == 'I' :
            heapq.heappush (max_hq,(-num,i))
            heapq.heappush(min_hq, (num,i))
            isLive[i] = True
            
        elif operation == 'D' :
            if num == 1 : # 최댓값 삭제
                clean_max (max_hq, isLive)
                if max_hq : 
                    _,i =heapq.heappop (max_hq)
                    isLive[i] = False
                
            else: # 최소값 삭제
                clean_min(min_hq, isLive) 
                if min_hq :
                    _,i = heapq.heappop(min_hq)
                    isLive[i] = False
                
        clean_max(max_hq, isLive)
        clean_min(min_hq, isLive)
    
    if not max_hq and not min_hq :
        return [0,0]
    
    return [-max_hq[0][0],min_hq[0][0]]