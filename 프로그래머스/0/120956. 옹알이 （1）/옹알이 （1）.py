def solution(babbling):
    answer = 0
    
    
    can_speak = ["aya", "ye", "woo", "ma"]
    
    can_all_speak = set()
    
    for string in babbling :
        if string in  can_speak :
            answer +=1
        else :
            temp = ""
            check = False
            for i in range(0, len(string)) :
                temp += string[i]
                if temp in can_speak :
                    temp = ""
                    check = True
           
                    
            
            if not temp :
                answer+=1
            
                    
                    
                
    return answer