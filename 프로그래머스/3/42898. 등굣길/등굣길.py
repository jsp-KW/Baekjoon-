def solution(m, n, puddles):
    answer = 0
    dp=[[0]*(m) for _ in range(n)]
    for p in puddles:
        x,y= p[0],p[1]
        dp[y-1][x-1]= -1
        
    dp[0][0]=1


    for i in range(0,n):
        for j in range(0,m):
            if i==0 and j ==0 : continue
            
            if dp[i][j]==-1:
                dp[i][j]=0
                continue
            
            down = dp[i-1][j] if i-1 >=0 else 0
            up = dp[i][j-1] if j-1 >=0 else 0
            
            dp[i][j] = (down+up)%1000000007
            
    answer= (dp[n-1][m-1])
    return answer