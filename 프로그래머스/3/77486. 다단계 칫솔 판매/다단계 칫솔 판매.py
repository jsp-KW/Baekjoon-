def solution(enroll, referral, seller, amount):
    answer = []
    # 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익 --> 10% 계산
    # 추천인한테 배분, 나머지 자신이 가짐
    
    # 판매수익 + 추천한 사람이 벌은 수익의 10%까지 이익
    # 10% 계산시 원단위에서 절사, 1원 미만 경우 자신이 모두 가짐
    
    
    # 개당 100원 
    
    n = len(enroll) 
    name_to_idx = { 
    
        name: i
        for i, name in enumerate(enroll)
    }
    
    parent = [-1] *(n) 
    
    for i in range (n) :
        if referral[i] != '-' :
            parent[i] = name_to_idx[referral[i]]
            
    profit = [0] *(n)
    for i in range (len(seller)) :
        current = name_to_idx[seller[i]]
        money = 100 * amount[i]
        
        while current != -1 and money >0 :
            give = money //10
            keep = money - give
            
            profit[current] += keep
            current = parent[current]
            money = give
    
    return profit
            
            
    return answer