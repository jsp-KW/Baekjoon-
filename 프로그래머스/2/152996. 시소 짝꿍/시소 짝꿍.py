from collections import Counter
def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    # 2,3,4
    # 탑승한 사람의 무게와 시소축과 좌석간의 거리의 곱이 양쪽 다 같은 경우
    
    
    
    # 몸무게 * 거리 = 상대 몸무게 * 거리
    unique_weights = sorted(counter.keys())
    
    for i in range (len(unique_weights)) :
        w1 = unique_weights[i]
        c1 =  counter[w1]
        
        if c1 >1 :
            answer += c1*(c1-1)//2
            
        for j in range (i+1, len(unique_weights)) :
            w2 = unique_weights[j]
            c2 = counter[w2]
            
            if (w2*2 == w1*3) or (w2*2 == w1* 4) or (w2*3 == w1*4) :
                answer+= c1 * c2
                
    return answer
    