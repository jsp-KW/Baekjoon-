import sys


N,M = map(int,sys.stdin.readline().split())

# (1,1) ->(N,M)
#(r,c) 면, r 만 이동, c만 이동, r,c 둘다 이동 총 3가지가 가능

dp = [[0]*(M+1) for _ in range (N+1)]

board =[[] for _ in range (N)]
for i in range (0,N) : 
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)

dp[1][1] = board[0][0] 

for i in range (N) :
    for j in range (M) :
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + board[i][j]


max_val = -1

for row in dp :
    temp = max(row)
    if temp > max_val :
        max_val = temp


print(max_val)