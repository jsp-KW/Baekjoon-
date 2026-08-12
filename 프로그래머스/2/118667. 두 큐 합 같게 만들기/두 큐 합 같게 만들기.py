from collections import deque
def solution(queue1, queue2):

    
    total_sum = sum(queue1) +  sum(queue2)
    
    if total_sum % 2 !=0 :
        return -1
    
    target = total_sum //2
    
    limit =  len(queue1) *4
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while cnt <= limit:
        if sum1 == target :
            return cnt
        if sum1 < target :
            value = q2.popleft()
            sum1+= value
            q1.append(value)
        else:
            value = q1.popleft()
            sum1 -= value
            q2.append(value)
            
        cnt +=1
    
    return -1
