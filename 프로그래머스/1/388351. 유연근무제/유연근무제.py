# 토요일, 일요일 -> 휴일이라 영향 X
# 1 : 월요일 ~  7 : 일요일
# 오전 9시 50분 -> 9*100 +50 해서 950

def add10min (time) :
    h = time //100
    m = time %100 +10
    
    if m >= 60 :
        h+=1
        m -=60
    return h*100 + m
def solution(schedules, timelogs, startday):
    # 직원 희망 출근 시간 스케쥴 배열에서 값을 가지고 온 후 +10해서 인정시각으로 만들기
    # schedules[0] -> 1번째 직원의 희망 출근시간
    loop_cnt = 0
    is_ok = 1
    answer = 0
    

    for i in range(0, len(schedules)): # 희망시간
        hope_time = add10min(schedules[i]) 
        is_ok = 1
        day = startday
        for j in range (0,7):# 실제 출근시간
            
            if day == 6 or day ==7 :
                pass
                
            else :
                if timelogs[i][j]>hope_time  :
                    is_ok =0
                    break

            day = (day %7)+1
        if is_ok ==1 :
            answer +=1
            
    return answer