def solution(n):
    answer = ''
    
    # 1->1
    # 2->2
    # 3->4
    
    # 4->11
    # 5->12
    #6 ->14
    
    #7 -> 21
    #8 -> 22
    #9 -> 24
    
    #10 -> 41
    #11 -> 111
    #12 -> 112
    #13 -> 114
    
    # 14 ->121
    #
    # 0,1,2
    # 1,2,4
    
    num = ["1","2","4"] 
    # 나머지가 1이면 1
    # 나머지가 2이면 2
    # 나머지가 0이면 4
    
    temp = n% 10
    while n >0 :
        temp = n %3 
        
        if temp == 1 :
            answer = "1" +answer
            n = n//3
        elif temp ==2 :
            answer = "2" +answer
            n = n//3
            
        elif temp ==0 :
            answer = "4" +answer
            n = n//3 -1
    
    return answer