import heapq
def solution(food_times, k):
    
    if sum(food_times) <= k :
        return -1 
    
    heap = []
    
    for i,food in enumerate(food_times) :
        heapq.heappush(heap, (food, i+1))
    answer = 0
    time = 0
    
    eaten_same = 0
    remain_foods_cnt = len(food_times)
    
    while heap :
        next_food_time = heap[0][0]
        
        need_to_eat = (next_food_time - eaten_same) *(remain_foods_cnt)
        
        if k >= need_to_eat :
            k-= need_to_eat 
            eaten_same=next_food_time 
            heapq.heappop(heap)
            remain_foods_cnt -=1
            
        else: 
            break
            
            
    remaining_food  =sorted(heap, key = lambda x : (x[1]))
    
    return remaining_food[k%remain_foods_cnt][1]
   