def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left =1
    right = distance
    cnt = 0
    
    while left <= right :
        
        mid = (left+right) //2 
        
        removed_rock = 0
        prev =0
        
        for rock in rocks :
            if rock-prev < mid :
                removed_rock +=1
            else :
                prev = rock
        
        if removed_rock <= n :
            answer = mid
            left= mid +1
            
        else :
            right = mid -1
            
        
        
    return answer

