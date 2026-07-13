def solution(n, s):
   
    #     # 집합 안 원소 개수가 n 개, 합이 s 인 집합들 중에, 각 원소의 곱이 최대가 되는 집합
    #     #  곱이 최대려면, 안의 원소들의 차이가 많이 나지않아야함.
 
    
    
    
    # n개의 수로 이루어진 집합
    # 합이 s가 되어야함
    
    if n>s :
        return [-1]
    else:
        # 맨 오른쪽부터면,... {s-1 ,1 } , {s-2, 2}, {s-3,3} , {s-4,4}.... 이런식으로 있다가 {1,s-1} 일텐데
        # {1,8} {2,7} {3,6} {4,5}
        
        #집합 개수는 s//n개일거같음
        default_val = s//n
        plus_cnt  = s%n
        
        res = [0]*(n)
        for i in range (n) :
            res[i] = default_val
        
        for i in range (n-1, -1, -1) :
            if plus_cnt ==0 :
                break
            res[i] +=1
            plus_cnt-=1
        
        return res
        
 