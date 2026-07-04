def solution(numbers):
    answer = []
    
    for num in numbers: 
        
        if num %2 ==0 :
            answer.append (num+1)
        else:
            temp = num
            cnt =0
            
            while temp% 2== 1:
                
                temp  = temp //2
                cnt +=1
            
            res = num + (2**(cnt)) - (2**(cnt-1))
            answer.append(res)
                
    return answer