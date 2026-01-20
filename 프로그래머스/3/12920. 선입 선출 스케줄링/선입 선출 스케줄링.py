def solution(n, cores):
    answer = 0
    
    # n 이 작업수
    # 코어 처리 시간이 담긴 배열 cores
    m = len (cores)
    
    if n <= m :
        return n 
    
    # t>=1 , n > m
    # t= 0 이후, 추가로 시작한 작업개수
    def done(t) :
        return m +  sum (t// c for c in cores)
    
    left, right = 0, max(cores) * n
    
    while left < right :
        mid = (left +right) //2
        if done(mid) >= n :
            right = mid
            
        else :
            left= mid +1
    
    t = left
    # t-1 시점에 할당된 작업 개수
    done_prev = m + sum ((t-1)// c for c in cores)
    
    for i, c in enumerate (cores) :
        if t%c ==0 :
            done_prev +=1
            if done_prev == n :
                return i +1
    
    
    