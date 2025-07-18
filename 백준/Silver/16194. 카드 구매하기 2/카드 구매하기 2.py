import sys
N = int(sys.stdin.readline())

cards_price= list(map(int, sys.stdin.readline().split()))

min_price = 0

# index+1개 비용  = cards_price[index]
# N개를 갖기 위해 지불해야하는 금액의 최솟값

dp = [0] * (N+1)

for i in range(1, N+1) :
    dp[i] = float('inf')
    for j in range (1,i+1):
        dp[i] = min(dp[i], dp[i-j] + cards_price[j-1])

print (dp[N])