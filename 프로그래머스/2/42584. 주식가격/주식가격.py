def solution(prices):
    answer = []
    # for i in range (len(prices)) :
    #     found = False
    #     for j in range (i+1, len(prices)) :
    #         if prices[i] > prices[j] :
    #             answer.append (j-i)
    #             found = True
    #             break
    #     if not found :
    #         answer.append(len(prices)-i-1)
    
    
    
    # 가격이 떨어지지 않은 기간은 몇초일까여
    
    # 자기 prices[i] 값보다 이후 나온값이 작아지지 않는 경우까지 구하기
    # 크거나 같으면 됨
    
    
    for i in range (0, len(prices)) :
        cnt = 1
        down_check = False
        for j in range (i+1, len(prices)) :
            
            if prices[i] <= prices[j] :
                cnt +=1
            else : # 떨어진거 확인
                down_check = True
                answer.append(cnt)
                break;
        if not down_check :
            answer.append(cnt-1)
                
                
                
    
    
    
    return answer