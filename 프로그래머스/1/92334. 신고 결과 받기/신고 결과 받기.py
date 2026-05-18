def solution(id_list, report, k):
    answer = []
    
    dic = {}
    
    for name in id_list : 
        if name not in dic :
            dic [name] = 0
            
    log = set()
    
    for r in report :
         
        user = r.split(" ")[0]
        target = r.split(" ")[1]
        
        if (user, target) not in log :
            dic [target] +=1
            log. add ((user,target))
        else :
            continue
            
    ben_list = set()
    
    for key, value  in dic.items():
        if value >=k  :
            ben_list.add(key)
     
   
    mail = {}
    # for name in id_list :
    #     cnt = 0
    #     for user, target in log :
    #         if user == name and target in ben_list: # ben 시킨 신고자마다 개수 count
    #             cnt +=1
    #     answer.append(cnt)
    
    for name in id_list :
        mail[name] =0
        
    for user, target in log :
        if target in ben_list :
            mail[user] +=1
    
    for _,value in mail.items() :
        answer.append(value)

    return answer