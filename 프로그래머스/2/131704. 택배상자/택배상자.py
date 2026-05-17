from collections import deque
def solution(order):
      
    answer = 0
    main_container = [i for i in range (1, len(order)+1)]
    temp_container = []
    check_idx = 0
    for target in order :
        if target not in temp_container :
            for i in range (check_idx, len(main_container)):
                temp_container.append(main_container[i])
                if target == main_container[i] :
                    check_idx = i+1
                    break
        

        if temp_container and temp_container[-1] == target :
            answer +=1
            temp_container.pop(-1)
        
        else:
            break
            
        
        
    return answer