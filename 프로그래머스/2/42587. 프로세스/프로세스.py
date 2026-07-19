
def solution(priorities, location):
    
    # 실행 대기큐의 프로세스 중요도가 담긴 배열
    # 몇번째로 실행되는지 알고싶은 프로세스의 위치 location
    # 
    
#     answer=0
#     queue = [(index, weight) for index,weight in enumerate(priorities)]
   
#     while True :
#         temp= queue.pop(0)
#         if any(temp[1]< q[1] for q in queue) :
#             queue.append(temp)
#         else:
#             answer+=1
#             if temp[0] == location :
#                 break
    
    
    
    
    answer = 0
    q = [(index, weight) for index, weight in enumerate(priorities)]
    
    while True:
        temp = q.pop(0)
        if any(temp[1] < t[1] for t in q) :
            q.append(temp)
        else:
            answer+=1
            if temp[0] == location:
                return answer
    
    
    
    
    
    
    
    
          
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
