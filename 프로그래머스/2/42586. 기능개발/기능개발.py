def solution(progresses, speeds):
    answer = []
    
    
    # 작업 남은거
    
    remains = []
    
    for i in range (0, len(progresses)) :
        remains.append( ((100- progresses[i]) // speeds[i], (100-progresses[i]) % speeds[i]))
    
      
    new_li = []
    for tup in remains :
        day = tup[0]
        remain = tup[1]
        if remain != 0 :
            day = day +1
            remain = 0
        
        new_li.append((day,remain))
            
  
    print("new", new_li)
    prev = new_li[0][0]
    cnt = 1
    for i in range(1, len(new_li)) :
        if prev >= new_li[i][0] :
            cnt +=1
        else :
            answer.append(cnt)
            cnt = 1
            prev = new_li[i][0]
            
    answer.append(cnt)
     
        
            
        
        
    
    
    return answer