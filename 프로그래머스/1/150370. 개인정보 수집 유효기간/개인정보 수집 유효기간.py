def solution(today, terms, privacies):
    answer = []
    # 모든 달은 28일 까지 있다고 가정한다
    # 유효기간은 3,6,12 개월이 있음
    
    today_calc  = today.split(".")
    today_year = int(today_calc[0])
    today_month = int(today_calc[1])
    today_day = int(today_calc[2])
    
    today_calc = ((today_year*(12))*28) + (today_month * 28) + (today_day)

    dic = {}
    for t in terms :
        temp = t.split(" ")
        check_type, val = temp[0],temp[1]
        dic[check_type] = int(val)
        
        
    cnt =0
    for info in privacies :
        cnt +=1
        day_info ,type = info.split(" ")
        year = int( day_info.split('.')[0])
        month = int( day_info.split('.')[1])
        day = int( day_info.split('.')[2])
        
        get_v = dic[type] *28 +day
        
        temp = ((year * 12)*(28) +  (month *28) + ( get_v))
        
   
        if today_calc >= temp :
            answer.append(cnt)
        
            
    return answer