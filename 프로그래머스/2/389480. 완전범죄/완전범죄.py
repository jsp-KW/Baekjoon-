def solution(info, n, m):
    answer = 0
    
    
    # A 도둑 잡히는 조건: 흔적개수 >=n
    # B 도둑 잡히는 조건: 흔적개수 >=m
    
    # info [i] -> [0] 이 A 도둑꺼 [1] 이 B도둑꺼
    
    # 구하고자하는 것 :  둘다 붙잡히지 않는 조건 아래에서 A도둑이 남긴 흔적의 최소 값은?
    
    
    # 완전 탐색 -> 2^40 => 시간 초과
    # A,B => A를 선택 OR 선택X 
    
    dp = [[False] *(m) for _ in range (n)]
    
    dp[0][0] = True # 처음에 0,0 아무도 안 훔쳤을때    
    for a_cost, b_cost in info :
        next_dp = [[False]*(m) for _ in range(n)]
        
        for a_trace in range(n) :
            for b_trace in range(m) :
                
                if not dp[a_trace][b_trace] :
                    continue
                    
                next_a = a_trace +a_cost 
                
                if next_a<n :
                    next_dp[next_a][b_trace] = True
                    
                next_b = b_trace + b_cost
                
                if next_b <m :
                    next_dp[a_trace][next_b] =True
                    
        dp = next_dp
    
    # True, False 경우의 수 True인 애들 중 가장 빠르게 return 될 수 있는 참인 경우 return,
    # a_trace 는 A 흔적의 최소개수
    for a_trace in range(n) :
        for b_trace in range(m):
            if dp[a_trace][b_trace] :
                return a_trace
            
    return -1