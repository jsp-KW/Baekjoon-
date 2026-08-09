def solution(n, k):
    answer = []
    
    nums = [i for i in range (1,n+1)]
    # nums[idx] 로 숫자 넣음
    def get_fact (n) :
        if n <=1:
            return 1
        else :
            return n*get_fact(n-1)
        
    k = k-1 
    while n > 0 :
        block = get_fact (n-1)
        idx =  k // block
        answer.append (nums.pop(idx))
        k = k % block # 자리 몇번째인지
        n-=1
    
    return answer