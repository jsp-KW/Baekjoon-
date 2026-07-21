import math
def solution(n, k):
    answer = []
    def make_num (num, k) :
        
        temp = ""
        while num !=0 :
            temp += str(num % k)
            num = num // k
        
        return temp[::-1]
    
    def check_num (num) :
        cnt = 0
        
        if num <=1 :
            return False
        
        for i in range (2, math.isqrt(num)+1) :
            if num % i ==0 :
                return False
            
        return True
    
            
    
    converted_num = make_num(n,k)
    
    #  소수 양쪽 0 있는 경우
    # 소수 오른쪽에만 0 왼쪽x
    # 소수 왼쪽 0 오른쪽 x
    # 양쪽 아무것도 없는 경우
    
    # 소수는 각 자릿수에 0을 포함하지 않는 수
    
    candidates = converted_num.split("0")
    
    real_cand = []
    
    for ch_num in candidates :
        if ch_num == "":
            continue
        if check_num (int(ch_num)) :
            real_cand.append(ch_num)
        else:
            continue
            
    answer = len(real_cand)
 
    
    
    return answer