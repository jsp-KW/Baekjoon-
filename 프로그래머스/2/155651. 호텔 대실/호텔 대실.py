import heapq

def solution(book_time):
    answer = 0
    # 퇴실시간 ~ 퇴실시간+10분 사용못함 이때까지
    # 최소 객실의 수
    
    book_time.sort (key = lambda x :(x[0]))
    
    change_time = []
    
    for start, end  in book_time :
        start_n = int (start.split(":")[0])*60 
        start_m = int (start.split(":")[1]) 
        
        s = start_n +start_m
        
        end_h = int (end.split(":")[0])*60
        end_m = int (end.split(":")[1])
        
        e = end_h +end_m+10
        
        change_time.append((s,e))
        
    rooms  = []
    
    for s,e in change_time :
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
        else :
            answer+=1
        heapq.heappush(rooms,e)
     

    return answer