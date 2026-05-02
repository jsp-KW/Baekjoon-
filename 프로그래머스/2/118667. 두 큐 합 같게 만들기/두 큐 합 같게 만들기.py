from collections import deque
def solution(queue1, queue2):
    answer = -2
    # 두 큐의 합 자체를 같게 만드는데 있어서, 작업을 최소화해야한다
    
    total_sum = (sum(queue1) + sum(queue2) )
    
    if total_sum %2 !=0  :
        return  -1
    
    target = total_sum //2 
    
    limit = len(queue1) *4

    count = 0
    
    q1= deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    
    
    while count <= limit :
        if sum1 == target :
            return count
        
        
        if sum1 < target :
            value = q2.popleft()
            sum1 += value
            q1.append(value)
        else :
            value = q1.popleft()
            sum1 -= value
            q2.append(value)
            
        count +=1
    
    
    
    return -1