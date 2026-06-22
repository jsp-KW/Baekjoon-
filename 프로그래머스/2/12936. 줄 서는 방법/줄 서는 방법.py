from itertools import permutations 

def solution(n, k):
    answer = []
    
    # n-1 개
    # 1개당, 그개 n개 * (n-1)!
    
    def fact (n) :
        if n <=1 :
            return 1
        else :
            return n* fact(n-1)
        
    k = k-1
    set_count = k // fact (n-1)
    
    
    nums = [i for i in range (1,n+1)]
    cnt = 1
    
    while n>0 :
        block = fact(n-1)
        idx= k // block
        answer.append(nums.pop(idx))
        k= k% block
        n-=1
    return answer