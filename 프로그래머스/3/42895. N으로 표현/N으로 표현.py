def solution(N, number):
    # 최소값이 8보다 크면 RETURN
    # DP[8] 까지
    
    dp = [set() for _ in range (9)]
    # dp[k] = dp[i] + dp[k-i]
    
    
    for k in range (1,9) :
        dp[k].add(int(str(N) * k))
        
        for i in range (1,k) :
            for a in dp[i] :
                for b in dp[k-i] :
                    dp[k].add(a+b)
                    dp[k].add(a-b)
                    dp[k].add(a*b)
                    if b!=0 :
                        dp[k].add(a//b)
                        
        if number in dp[k]:
            return k
    return -1