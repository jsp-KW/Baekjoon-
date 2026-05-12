def solution(want, number, discount):
    answer = 0
    
    #  10일동안회원 자격을 부여한다
    # 할인 제품 하나씩 구매 가능
    # 10일 연속으로 일치하는 경우 회원가입
    
    dic = {}
    
    for i in range (0, len(want)) :
        dic [want[i]] = number[i]
    
    
    correct = 0 
    # 14 -10 +1
    # day = i+1
    for i in range (len(discount) -10 +1) :
        target = discount[i:10+i]
        temp = dic.copy()
        
        for t in target :
            if t in temp :
                temp[t] -=1
                if temp[t] == 0 :
                    del temp[t]
            else :
                continue
                
        if not temp :
            answer +=1
        
    
    return answer