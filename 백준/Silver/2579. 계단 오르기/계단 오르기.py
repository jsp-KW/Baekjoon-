import sys


N = int(sys.stdin.readline())

dp = [0] *(N+1)
scores = [0]
for _ in range (N) :
    score = int(sys.stdin.readline())
    scores.append(score)
dp[0] = 0
dp[1] = scores[1]

if N >=2 :
        dp[2]= scores[1] + scores[2]

for i in range (3,N+1) :
    # 두번째 경우는 i-3칸까지 오고, i-2 칸 제외후, i-1칸에서 한칸 움직인 경우
    dp[i] = max (dp[i-2]+ scores[i], dp[i-3]+ scores[i-1]+ scores[i])


print (dp[N])