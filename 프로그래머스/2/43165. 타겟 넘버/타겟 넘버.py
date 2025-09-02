from collections import deque

def solution(numbers, target):
    answer = 0
    #더하거나, 빼거나 ->2가지
    #numbers 배열의 길이가 5라면, 2^5이므로,
    # 길이가 n일때 2^n
    #적절히 숫자 조합하여, 그 합이 target이 되도록
    que = deque()
    calc_value = 0
    
    que.append((0,0))
    while que :
        total_sum, cur_idx = que.popleft()
        
        if cur_idx == len(numbers) :
            if total_sum == target :
                answer+=1
                
        else:
            que.append((total_sum + numbers[cur_idx], cur_idx+1))
            que.append((total_sum - numbers[cur_idx], cur_idx+1))
                
        
    return answer