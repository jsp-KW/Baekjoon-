import sys

# 과일 -> 길이 +1
# i번째 과일 높이 hi
# 자신의 길이보다 작거나,같은 높이 과일 먹을 수 있음
# L ->  과일들을 먹어서 성장할 수 있는 최대 길이


N, L = map(int,sys.stdin.readline().split())

heights = list(map(int,sys.stdin.readline().split()))

heights.sort()

for h in heights :
    if h <= L  :
        L= L+1 
    else:
        break

print(L)