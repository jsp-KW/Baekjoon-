def solution(n):
    answer = 0
    
    # 가로가 2, 세로가 1 직사각형 모양의 타일# 2
    # 세로가 2이고 가로의 길이가 n인 바닥을 가득 채우려한다 = 2n
    
    # 채우는 방법 가로 or 세로
    
    # dp[i] = 2x i 의 바닥을 채우는 수(i는 가로)
    # 2 2 2
    dp = [0]*(n+1)
    dp[0] =0
    dp[1] =1
    dp[2] =2
    dp[3] =3 
    
    for i in range (4,n +1) :
        dp[i] = (dp[i-1] +dp[i-2])%1000000007
        
    return dp[n]