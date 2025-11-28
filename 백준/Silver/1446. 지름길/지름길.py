import sys

# 지름길의 개수 N 과 고속도로 길이 D

# 지름길의 시작위치 , 도착위치 지름길 길이
# 거리의 최솟값을 출력

N, target_dist = map(int, sys.stdin.readline().split())

short_road= []
answer =0
for _ in range(N) :
    start, end, dist = map(int,sys.stdin.readline().split())
    if end <= target_dist :
        short_road.append((start,end,dist))


dp = [float('inf')]*(target_dist+1)
dp [0]=0


for  i in range (1, target_dist+1):
    dp [i] = min (dp[i], dp[i-1]+1)

    for s, e, d in short_road :
        if e ==i :
            dp[i] = min(dp[i], dp[s]+d)



print (dp[target_dist])