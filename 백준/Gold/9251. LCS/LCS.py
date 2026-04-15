import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

# dp [i][j] -> str1 에서 i개 , str2 에서 j개
# 이 둘의 lcs 길이
n= len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range (n+1)]


# dp[1][1] ~ dp[n][m] 까지 계산
for i in range (1,n+1):
    for j in range (1,m+1) :
        if str1[i-1] == str2[j-1] :
            dp[i][j] = dp[i-1][j-1] +1

        else :
            dp[i][j] = max(dp[i][j-1] , dp[i-1][j])


print(dp[n][m])