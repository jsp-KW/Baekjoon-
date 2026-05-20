def solution(food):
    answer = ''
    
    left= ""
    right =""
    for i in range (1, len(food)) :
        if food[i] % 2==0 :
            continue
        else :
            food[i] = food[i] -1
    
    print(food)
    for i in range (1, len(food)):
        cnt = food[i] //2 
        
        for _ in range (cnt) :
            left += str(i)
    

    right = ''.join (reversed(left))
    answer+=left
    answer +='0'
    answer += right
        

    return answer