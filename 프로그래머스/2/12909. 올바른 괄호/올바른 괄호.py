def solution(s):
    answer = True
    stack=  []
    for ch in s :
        if ch == '(' :
            stack.append(ch)
        elif ch == ')' :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
                answer =True
    
    if len(stack) == 0 and answer :
        return True
    
    else :
        return False
        
                
