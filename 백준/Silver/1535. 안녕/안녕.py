import sys

N = int(sys.stdin.readline())

how_many_lose=list(map(int,sys.stdin.readline().split()))
how_many_happy=list(map(int,sys.stdin.readline().split()))

dp=[0]*100

for i in range(N):
    lose= how_many_lose[i]
    happy= how_many_happy[i]

    for j in range(99,lose-1,-1):
        dp[j]= max(dp[j],dp[j-lose]+happy)


print(max(dp))