from itertools import product # 중복 허용 + 자리 가능
def solution(users, emoticons):
    answer = [0,0]
    
    sales = [10,20,30,40]
    
    for sale_case in product(sales,repeat=len(emoticons)) :
        plus_count =0
        total_price =0
        
        for user_sale, user_limit in users: # 비율, 가격
            user_price = 0
            
            for i in range (len(emoticons)) :
                sale = sale_case[i] # 할인율 조합 한개
                
                if sale >= user_sale : # 유저의 비율보다 할인율 조합이 크거나 같은 경우 산다
                    user_price += emoticons[i]* (100-sale) //100
                    
            if user_price >= user_limit : # 유저가 제한선보다 크거나 같으면 이모티콘 서비스 가입
                plus_count +=1
            else :# 아니라면, 구매만 (가입은 안한다)
                total_price += user_price
        
        if plus_count > answer[0]:
            answer = [plus_count, total_price]
        elif  plus_count == answer[0] and total_price> answer[1]:
            answer = [plus_count, total_price]
    return answer