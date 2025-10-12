import sys

N = int (sys.stdin.readline())

dp = [0] *(N+2)

data = [0]
for _ in range (N) :
    T,P = map(int,sys.stdin.readline().split())
    data.append((T,P))


for i in range (1,N+1) :
    
    if i+ data[i][0] <= N+1 : # 상담을 선택했을때
        dp[i+data[i][0]] = max (dp[i+data[i][0]], dp[i]+data[i][1])

    dp[i+1] = max(dp[i+1], dp[i]) # SKIP  하는 거

print (dp[N+1])