import sys

# 부분 수열 중 가장 합이 큰것을 구하자

# j<i  A[j] <A[i] - > dp[i] = max (dp[i], dp[j] +A[i])


n = int (sys.stdin.readline())

nums = list (map(int,sys.stdin.readline().split()))

dp = [0]*(n)
dp [0] = nums[0]

for  i in range (1, n) :
    dp[i] = nums[i]

    for j in range (0,i) :
        if nums[j] < nums[i] : # j까지의합 +  i번째 숫자 or i번째 값
            dp[i] = max (dp[i], dp[j] + nums[i])


print(max(dp))