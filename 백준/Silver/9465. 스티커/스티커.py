import sys

T = int(sys.stdin.readline())
answer = []
for _ in range (T): 
    
    col_len = int (sys.stdin.readline())

    top = [0] + list (map(int, sys.stdin.readline().split()))
    bottom = [0] + list(map(int,sys.stdin.readline().split()))

    dp = [[0]*(col_len+1) for _ in range (2)]

    dp[0][1] = top[1]
    dp[1][1] = bottom[1]


    for i in range (2,col_len+1) :
        dp[0][i]=  max(dp[1][i-1], dp[1][i-2]) + top[i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + bottom[i]

    answer.append(max(dp[0][col_len],dp[1][col_len]))

for a in answer:
    print (a)
