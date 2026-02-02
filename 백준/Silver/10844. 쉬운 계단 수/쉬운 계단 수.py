import sys

N= int(sys.stdin.readline())

dp =[[0]*(10) for _ in range(N+1)]

#dp[i][j]= 길이가 i이며 끝j로 끝나는경우

for i in range(1,10):
    dp[1][i]= 1

for i in range (2,N+1):
    for j in range(0,10):
        if j ==0:
            dp[i][j]= dp[i-1][1]

        elif j==9:
            dp[i][j]= dp[i-1][8]

        else:
            dp[i][j]= (dp[i-1][j-1]+dp[i-1][j+1]) %1000000000#옆, 왼 -1 오 +1

print(sum(dp[N])%1000000000)