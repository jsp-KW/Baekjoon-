def solution(m, musicinfos):
    answer = ''
    # 12개의 음.
    # 재생 시작~ 끝 , 음악 제목, 멜로디 악보로 구성되어있다
    # 악보에 사용되는 음은 12개
    # 음은 1분에 1개씩, 음악 길이 < 재생 시간 : 처음부터 다시 반복,  <=> 반대 경우 : 재생 시간만큼만 재생
    # 00:00 을 넘기진 않음
    # 없는 경우 " " 을 반환
    # 조건이 일치하는 음악이 여러개일 경우, 재생된 시간이 제일 긴 음악 제목을 반환하고, 시간이 같은 경우 먼저 입력된걸
    
    # 네오가 기억한 멜로디 : m
    
    #  #case를 바꿔버리자
    
    # 아 ,,, # 붙으면 바로 소문자로 치환해버리기
    
    
    neo_melodie = len(m) 
    answer_candidates = []
    idx= 0
    
    def remove_shap (melodie) :
        return melodie.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    
    
    m = remove_shap(m)
    
    
    for music_info in musicinfos :
        
        start_t , end_t , title, melodie = music_info.split(',')
        
        melodie = remove_shap(melodie)
        
        start_h = int(start_t.split(':')[0]) *60
        start_m = int(start_t.split(':')[1])
        
        end_h = int(end_t.split(':')[0])*60
        end_m = int(end_t.split(':')[1])
        
        time_diff =  (end_h + end_m) - (start_h+start_m)
        save_time_diff= time_diff
        
        temp = (time_diff // len(melodie)) 
        time_diff %= len(melodie)
        temp_rest = time_diff
        
        temp_str = melodie * temp + melodie[:temp_rest]
        
        if m in temp_str :
            answer_candidates.append((title,save_time_diff, idx))
        else:
            continue
        
        idx = idx +1
    
    if not answer_candidates  :
        return "(None)"
    
    answer_candidates.sort(key= lambda x : (-x[1], x[2]))
    
    return answer_candidates[0][0]