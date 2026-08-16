from itertools import combinations

def solution(nums):
    answer = 0
    
    def check_num (target) :
        cnt = 0
        for i in range (1, target+1) :
            if target % i ==0 :
                cnt +=1
        
        if cnt >2 :
            return False
        else :
            return True
    
    for comb in combinations (nums, 3) :
        target_num = 0
        for c in comb :
            target_num +=c
        
        if not check_num(target_num) :
            continue
        else:
            answer+=1
            
    return answer
    
 