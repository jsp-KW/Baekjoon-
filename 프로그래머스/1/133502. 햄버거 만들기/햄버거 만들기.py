
def solution(ingredient):
    # 빵 - 야채- 고기 -빵
    
    # 1 : 빵 2:야채  3: 고기
    # 1 2 3 1 순으로 들어와야함
    
    answer = 0
    # 9
    # 5
    

    stack =[] 
    
    for num in ingredient :
        stack.append(num)
        
        if len(stack) >=4 :
            target = stack [-4:]
            if target == [1,2,3,1] :
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer+=1
            else :
                continue
 
                
            
            
            
    return answer