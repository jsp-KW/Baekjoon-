import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dp = [1]*(N) 


for i in range (N):
    for j in range (i) :
        if nums[i] > nums[j] :
            dp[i] = max(dp[i], dp[j] +1)

print(max(dp))

#nums[i]가 마지막으로 끝나는 수열의 길이를 저장할 dp 테이블
#i 직전까지 j로 돌리고, 붙이면서 값이 nums[i]보다 작으면 조건 만족해서 길이 +1
