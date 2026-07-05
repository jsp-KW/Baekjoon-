def solution(plans):
    answer = []
    
    # 새로운 과제를 시작할 ㅅ간-> 기존 진행과제 멈추고 새로운 과제 시작
    # 진행 과제 끝내면 멈춘 과제 이어서
    # 새로 시작 과제 + 멈춘 과제 두가지 있는 경우:  시작 해야하는 과제부터
    
    
    change_plans = []
    
    for p in plans :
        subject, start_time, progress_time = p[0],p[1],p[2]
        start_time = int (start_time.split(":")[0]) *(60) + int(start_time.split(":")[1])
        change_plans.append((subject, start_time, int(progress_time))) # 과목/시작시간/소요 시간
    
   
    #정렬
    
    change_plans.sort (key= lambda x : (x[1]))
    
    
    # 꺼내고, 다음 과제 시작시간이 현재 시작 과제를 마치기까지의 시간 사이라면 일단 중단하고 스택에 삽입
    
    temp_stack = []
    for i in range (0,len(change_plans)-1) :
        next_assignment = change_plans[i+1]
        cur_assignment = change_plans[i]
        if cur_assignment[1]+ cur_assignment[2]  > next_assignment[1] : # 과목/ 얼만큼 진행했는지 현재과제를 마치기 위한 시간 계산후 스택에 저장
            temp_stack.append ((cur_assignment[0], cur_assignment[2] - (next_assignment[1] - cur_assignment[1])))
        
        else:
            answer.append (cur_assignment[0])
            
            remain_time = next_assignment[1] - (cur_assignment[1] + cur_assignment[2])
            
            while temp_stack and remain_time > 0 :
                doing_name, doing_time = temp_stack.pop()
                
                if doing_time <= remain_time :
                    answer.append(doing_name)
                    remain_time -= doing_time
                
                else :
                    temp_stack.append((doing_name, doing_time-remain_time))
                    remain_time = 0
    
    answer.append(change_plans[-1][0]) # 마지막 과제 처리 : 새로 시작하는 과제가 멈춘 과제보다 빨리 진행되어야함
    
    
    # 멈춘 남은 과제들 처리
    while temp_stack :
        name, time = temp_stack.pop()
        answer.append(name)
            
            
        
        
    
    return answer