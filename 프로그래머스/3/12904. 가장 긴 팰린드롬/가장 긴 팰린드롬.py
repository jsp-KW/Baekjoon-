def solution(s):
    answer = 0
 
    # 홀수 : ab c ba 중심 위치 : len // 2 +1
    # 짝수 : abba  중심이 두개
    
    # 중심 i -> left,right 기준으로 해서  두가지 while 문으로 돌아서 체크해야함.
    max_len= 0
    for i in range(0, len(s)):
        left= i
        right = i
        
        while (left >=0  and right <=len(s) -1) and s[left] == s[right] :
            answer = max(answer, right-left +1)
            left-=1
            right+=1
           
        left= i
        right = i+1
        
        while (left >=0 and right <= len(s)-1) and s[left]== s[right] :
            answer = max(answer, right-left +1)
            left-=1
            right +=1
       
        
    
    return answer