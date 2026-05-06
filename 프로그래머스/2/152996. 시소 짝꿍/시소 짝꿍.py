from collections import Counter 
def solution(weights):
    answer = 0
    
    counter = Counter (weights)
    # 2,3,4
    # 탑승한 사람의 무게와 시소축과 좌석간의 거리의 곱이 양쪽 다 같은 경우
    
    
    # 100 100 180 270 360
    
    for w in counter :
        c = counter[w]
        
        answer +=  c* (c-1) //2 
        
        if w * 2 in counter :
            answer +=  c* counter[2*w]
            
        if (3*w) %2 == 0 :
            target = (3*w) //2 
            if target in counter :
                answer += c * counter [target]
                
        if (4*w) %3 ==0 :
            target= (4*w) //3 
            if target in counter :
                answer += c * counter[target]
    return answer