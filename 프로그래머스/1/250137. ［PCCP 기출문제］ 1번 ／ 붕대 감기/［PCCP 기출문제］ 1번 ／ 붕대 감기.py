def solution(bandage, health, attacks):
    answer = 0
    
    # t초동안 감으면서 x만큼 회복
    # t초만큼 성공시 y만큼 추가회복
    
    # 최대체력 존재
    
    # 공격 당하면 기술 취소
    # 공격 당하는 순간 회복 x
    # 공격당해 기술 취소 or  기술 끝나면 붕대 감기를 다시 사용 -> 연속 성공시간 0
    
    #죽으면 -1, 모든 공격 끝난 직후 남은 체력 return
    
    # bandage [시전시간, 초당회복량, 추가회복량]
    # health 체력
    # attacks 

    time_limit = attacks[len(attacks)-1][0]
    
    max_health = health
    idx = 0
    time =1
    successive_heal = False
    duration_time =0
    while time <= time_limit :
        
        attack_time = attacks[idx][0]
        attack_amount = attacks[idx][1]
        if time == attack_time :
            health = health - attack_amount
            duration_time = 0
            if health <=0 :
                return -1
            
            idx+=1
        else:
            duration_time +=1
            if duration_time == bandage[0] :
                health = health + bandage[1] + bandage[2]
                duration_time = 0
            else:
                health = health + bandage[1]
            
            if health > max_health :
                    health = max_health
                    
        time+=1
        
        
    return health