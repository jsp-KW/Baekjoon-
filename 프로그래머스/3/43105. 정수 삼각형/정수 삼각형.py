def solution(triangle):
    answer = 0
    # i,j -> 왼쪽은  i-1, j-1 , 오른쪽은 i-1,j
    # dp[i][j] = max (dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] 
    
    # dp[0][0] = root =  triangle[0][0]
    # 끝쪽은 부모가 하나임, 왼쪽 끝 dp[i][0] =  dp[i-1][0] + triangle [i][0]
    # 오른쪽 dp[i][i] = dp[i-1][i-1] + triangle [i][i]
    
    
    height = len (triangle)
    dp  = [[0]*(i+1) for i in range (0,height)]
    
    dp[0][0] = triangle [0][0]
    #초기값 정의
    for i in range (1,height) :
        
        dp[i][0] = dp[i-1][0] + triangle[i][0] #왼쪽 끝점
        
        dp[i][i] = dp[i-1][i-1] + triangle[i][i] # 오른쪽 끝점
        
        for j in range (1,i) :
            dp[i][j] = max (dp[i-1][j-1], dp[i-1][j]) +  triangle[i][j]
        
    return max(max(dp))