def solution(s):
    answer = float('inf')
    #2이상인 애들은 압축해서 aa-> 2a
    # 압축률이 낮음 -> 1개 이상의 단위로 잘라서 압축 가능한 더 짧은 문자열로 
    n = len(s)
    max_len =  n//2
    
    if len (s) == 1 :
        return 1
    
    target_len = 1
    while target_len <= max_len :
        compressed = ""
        prev = s[0:target_len]
        cnt =1 
        
        for i in range (target_len,n,target_len) :
            cur = s[i:i+ target_len]
            
            if cur == prev :
                cnt +=1
            else:
                if cnt >=2 :
                    compressed += str(cnt)
                
                compressed +=prev
                prev = cur 
                cnt =1
        
        # 마지막 문자열 처리
        if cnt >=2 :
            compressed +=str(cnt)
        
        compressed += prev
        
        target_len +=1
        answer = min(answer, len(compressed))       
        
    return answer