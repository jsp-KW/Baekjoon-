import heapq

def solution(scoville, K):
    answer = 0
    
    # 가장 맵지 않은거 +  (두 번째로 맵지않은 거 * 2) = 섞은 음식.
    heapq.heapify(scoville)
    
    while scoville and scoville[0] < K:
        if len(scoville) < 2 :
            return -1
        
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        temp = first + (second*2)
        
        heapq.heappush(scoville, temp)
        answer+=1
            
    return answer