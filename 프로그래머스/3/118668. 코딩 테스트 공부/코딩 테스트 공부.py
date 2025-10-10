def solution(alp, cop, problems):
    answer = 0
    
        # 알고력/코딩력/증가하는 알고력/ 증가하는 코딩력 / 문풀시간
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    alp = min (alp, max_alp)
    cop = min (cop, max_cop)
    
    
    MAX_VALUE = float('inf')
    dp = [[MAX_VALUE] * (max_cop +1 ) for _ in range (max_alp +1)]
    
    
    dp[alp][cop] = 0
    
    for a in range (alp,max_alp +1) :
        for c in range (cop, max_cop+1) :
            
            if a+1 <= max_alp:
                dp[a+1][c] = min (dp[a][c]+1 , dp[a+1][c])
            if c+1 <= max_cop :
                dp[a][c+1] = min(dp[a][c]+1, dp[a][c+1])
            
            for req_a, req_c, reward_a,reward_c, cost in problems:
                if a>= req_a and c >= req_c :
                    new_alp = min (max_alp, a+reward_a)
                    new_cop = min(max_cop, c+reward_c)
                    dp[new_alp][new_cop] = min (dp[new_alp][new_cop], dp[a][c] + cost)
                    
                    
    return dp[max_alp][max_cop]