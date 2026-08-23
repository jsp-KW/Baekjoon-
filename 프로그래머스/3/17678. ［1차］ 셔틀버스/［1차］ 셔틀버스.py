def solution(n, t, m, timetable):
    answer = ''
    # 콘이 셔틀을 타고 갈수있는 도착시간 중 제일 늦은 시각 구하기
    # 23:59에 집 돌아감,
    # N회 T분 M명
    
    # 정원이 m명인데..
    
    # BUS : 9:00
    
    time_to_min = []
    for temp in timetable :
        hour = temp.split(":")[0]
        minute=  temp.split(":")[1]
        total = int(hour) *60 + int(minute)
        time_to_min.append(total)
    
    time_to_min.sort () # 정렬해주고,
    time = 1
    first_bus = 9 * 60
    wait_idx = 0
    temp_answer =0
    
    for bus in range (n):
        now_bus_time = first_bus + bus * t
        cnt = 0
        while wait_idx < len(time_to_min) and cnt < m:
            if time_to_min[wait_idx] <=now_bus_time :
                wait_idx +=1
                cnt +=1
        
            else: break
    
    if bus == n -1 :
        if cnt +1 <= m :
            temp_answer = now_bus_time
        else :
            temp_answer = time_to_min[wait_idx-1]  -1 # 막차탄 마지막 사람보다 1분 빨리가기 여기 어렵네
        
    get_hour = (temp_answer//60)
    
    if get_hour <10:
        get_hour = "0"+ str(get_hour)
    else :
        get_hour = str(get_hour)
    
    get_min = (temp_answer%60)
    
    if get_min <10 :
        get_min ="0" + str(get_min) 
    else:
        get_min = str(get_min)
    
    
    answer = get_hour + ":" +get_min
    
    
    
        
    
    return answer