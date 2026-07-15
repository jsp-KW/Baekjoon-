def solution(n, t, m, p):
    answer = ''

    
    
    temp = []
    
    
    def convert_num(n, num) :
        digits = "0123456789ABCDEF" #10,11,12,13,14,15
    # 2~16 진법 변환 함수
        res= ""
        if num == 0 :
            return  "0"
        
        while num != 0 :
            res += digits[num%n]
            num= num //n
        
        return res[::-1] # 뒤집어서 
    
    
    target_num = 0
    idx = 0
    
    #n : 진법 t : 튜브가 말해야하는 숫자 개수 m: 참가인원,  튜브 순서 p
  
    # idx + (m *t) -1 인 지점??에서 발언?
    # p-1
    # p-1 +m
    # p-1 +2m
    # p-1 +3m
    # p-1 + i*m 
    last_idx = (p-1) + (t-1) * m
    temp_str = ""
    while len(temp_str) <= last_idx  :
        convert_res = convert_num(n,target_num)
        temp_str += convert_res
        target_num+=1
        
                    
    for i in range (t) :
        idx = (p-1) + i*m
        answer+= temp_str[idx]
        
    return answer