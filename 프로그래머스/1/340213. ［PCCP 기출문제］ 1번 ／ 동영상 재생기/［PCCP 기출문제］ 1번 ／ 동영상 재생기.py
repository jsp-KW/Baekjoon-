def solution(video_len, pos, op_start, op_end, commands):
    
    
    # 10초 전 이동, 후 이동, 오프닝 건너뛰기
    
    # 10초전 이동 : 현재위치 10초 미만 경우-> 처음위치 :0분 0초
    # 10초 후 이동 : 남은시간 10초미만인 경우 -> 마지막 위치 : 동영상 길이
    # 오프닝 건너뛰기 : 자동으로 오프닝 끝나는 위치로 
    
    # pos가  op_start  <= pos <= op_end 라면, 먼저 처리해주고, 그다음 적용
    
    
    #초 단위로 바꾸기,
    video_len = (int (video_len.split(":")[0]) *(60) )+  int (video_len.split(":")[1]) 
    pos = (int (pos.split(":")[0]) *60 )+ int (pos.split(":")[1]) 
    op_start = (int (op_start.split(":")[0] )* (60)) + int (op_start.split(":")[1])
    op_end = (int (op_end.split(":")[0]) *(60)) + int (op_end.split(":")[1])
    
    
    def is_in_opening (time) :
        if op_start <= time <= op_end :
            return op_end 
        else :
            return time
    pos =is_in_opening(pos)
    for com in commands:
        if com == 'prev' :
            if pos <= 10 :
                pos = 0
            else :
                pos = pos -10
            
            
        elif com =='next' :
            if pos +10 >= video_len :
                pos = video_len
            else:
                pos = pos +10
                
        pos =is_in_opening(pos)
    
    minutes = pos //60 
    seconds = pos % 60
    
    if minutes < 10 :
        answer  =  "0"+str(minutes) +":"
    else:
        answer = str(minutes) + ":"
    
    if seconds  <10 :
        answer += "0" +str(seconds)
    else :
        answer+= str(seconds)
        
    
    return answer