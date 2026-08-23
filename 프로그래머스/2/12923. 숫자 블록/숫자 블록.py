import math
def solution(begin, end):
    answer = []
    
    
    # 약수 중 가장 큰 약수, 자기자신 제외하고
    for num in range (begin, end +1) :
        block_num = 1
        
        if num ==1 :
            answer.append(0)
            continue
        
        for j in range (2,int(math.sqrt(num)) +1) :
            if num% j ==0 :
                temp = num //j
                
                if temp <= 10000000 :
                    block_num = temp
                    break
                
                block_num = j
            
                
                
        
        answer.append (block_num)
    return answer