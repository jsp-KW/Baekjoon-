import sys

n = int (sys.stdin.readline())
cnt = 0    

dp = [0]*(n+1)


# 호출횟수저장
# 0일때는 1번 1일때는 1번
# 2일때는 1번 3일때는 dp[2], dp[1] 에 자기자신 한번 호출 즉 3번
#  3일땐, dp[3]-> dp[2] +dp[1] ->dp[1]+dp[0] + dp[1] 5번
# 4일땐 -> dp[4] -> dp[3]+dp[2] -> dp[2]+dp[1] +dp[2]+dp[1]-> 8번 즉 dp[3] +dp[2] 에 본인 호출 +1 총 9번
if n<=1 :
    print(1)
else:
        
    dp[0]=1
    dp[1]=1

    for i in range (2,n+1) :
        dp[i] = dp[i-1]+ dp[i-2] +1

    print(dp[n]%1000000007)