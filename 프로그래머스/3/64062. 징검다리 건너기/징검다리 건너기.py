def solution(stones, k):
    
    # 연속으로 못밟는 돌이 k개 연속되면 못감
    
    answer = 0
    break_check = False
    
    left = 1
    right = max(stones)
    
    while left<=right:
        mid = (left+right)//2
        if can_cross(stones,k, mid): # 3
            answer = mid
            left = mid+1
        else:
            right= mid-1
    return answer

def can_cross(stones, k, people) :
    broken = 0
    for stone in stones:
        if stone <people:
            broken +=1
            if broken >= k: # 
                return False
        else:
            broken=0
    
    return True
                          
                    
