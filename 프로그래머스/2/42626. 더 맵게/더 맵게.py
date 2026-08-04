import heapq

def solution(scovile, K):
    answer = 0
    # K이상 될때까지 반복해서 섞기
    heapq.heapify(scovile)
    
    
    while len(scovile) >=2 and scovile[0] <K:
        first = heapq.heappop(scovile)
        second = heapq.heappop(scovile)
        temp = first + (second * 2)
        heapq.heappush(scovile, temp)
        answer+=1
    
    
    if scovile[0] >= K :
        return answer
    else:
        return -1