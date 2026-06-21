import heapq
def solution(n, k, enemy):
    answer = 0
    
    # 무적권 k번 사용
    # 몇 라운드까지 막을 수 있는지?
    heap = []
    
    for index, ene in enumerate(enemy):
        heapq.heappush(heap, ene)
        
        if len(heap) > k:
            n -= heapq.heappop(heap)
        
        if n < 0:
            return index
    
    return len(enemy)